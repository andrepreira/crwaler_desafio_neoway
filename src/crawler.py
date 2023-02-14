import re
from typing import Tuple

import requests
import pandas as pd
from bs4 import BeautifulSoup

URI_CORREIOS="https://www2.correios.com.br/sistemas/buscacep"

class Crawler:
    def __init__(self):
        self.url_uf = URI_CORREIOS + "/buscaFaixaCep.cfm"
        self.url_busca = URI_CORREIOS + "/resultadoBuscaFaixaCEP.cfm"
        
    def find_uf(self) -> list:

        response = requests.get(self.url_uf)
        if response.status_code != 200:
            raise Exception(f"Não foi possível buscar os UFs")
        soup = BeautifulSoup(response.content, "html.parser")
        options_list = soup.find("select").find_all("option", attrs={"value": re.compile(r"^[A-Z]{2}$")})
        return [uf.get_text() for uf in options_list if uf != " "]

    def search_datas(self, uf_list: list) -> Tuple[list, list]:
        uf_error = []
        datas = []
        for uf in uf_list:
            response = requests.post(self.url_busca, data={"UF": uf})
            if response.status_code != 200:
                raise Exception(f"Não foi possível buscar o html das tabelas") 
            soup = BeautifulSoup(response.content, "html.parser")
            if soup.find("strong"):
                uf_error.append(uf)
                print(f'\n the UF {uf} do not was searched ! ')
                continue
            if soup.find("em"):
                uf_error.append(uf)
                print(f'\n the UF {uf} do not was searched ! ')
                continue
            datas.append({
                "UF": uf,
                "Localidade": [x.get_text() for x in soup.find_all("table")[1].find_all("td")[0::4]],
                "Faixa de CEP": [x.get_text() for x in soup.find_all("table")[1].find_all("td")[1::4]]
            })
        return datas, uf_error
    def dataframe(self, df: pd.DataFrame, datas: list) -> pd.DataFrame:
        for data in datas:
                df = pd.concat([df, pd.DataFrame(data)], ignore_index=True)
        return df
                    
    
    def execute(self):
        # Get UFs
        uf_list = self.find_uf()
        df = pd.DataFrame([])
        cont = 0
        cont_limit = 10
        while True:
            datas, uf_error  = self.search_datas(uf_list)
            df = self.dataframe(df, datas)
            cont+=1            
            print(f"UFs not searched in try number {cont}: {uf_error}")
            if not uf_error:
                break
            if cont == cont_limit:
                exit(f"Error: The limit of {cont_limit} tries was reached")
                
            uf_error = uf_list
        df = df.drop_duplicates()
        df['id'] = df.index
        df.to_json(
                   path_or_buf=f'./src/output.jsonl',
                   lines=True, 
                   orient='records'
        )
        print(df)
if __name__ == '__main__':
    Crawler().execute()
        