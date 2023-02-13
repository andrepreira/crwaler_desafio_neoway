import unittest
from unittest.mock import patch
import pandas as pd

from src.crawler import *

class TestCrawler(unittest.TestCase):

    def setUp(self):
        self.crawler = Crawler()

    def test_find_uf(self):
        with patch("requests.get") as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.content = '<html><select><option value="AC">AC</option><option value="AL">AL</option></select></html>'
            result = self.crawler.find_uf()
            self.assertEqual(result, ['AC', 'AL'])

    def test_search_datas(self):
        with patch("requests.post") as mock_post:
            mock_post.return_value.status_code = 200
            mock_post.return_value.content = '''
                <table class="tmptabela" style="width:27%">
                <tbody><tr>
                    <th><b>UF</b></th>
                    <th><b>Faixa de CEP</b></th>	
                    </tr>
                    <tr>
                    <td width="10">AC</td>
                    <td width="90"> CEP</td>	
                    </tr>
                </tbody></table>
                <table class="tmptabela">
                    <tbody><tr></tr>
                    <tr>
                    <th><b>Localidade</b></th>
                    <th><b>Faixa de CEP</b></th>	
                    <th><b>Situação</b></th>	
                    <th><b>Tipo de Faixa</b></th>	
                    </tr>	

                    <tr bgcolor="#C4DEE9">

                    <td width="100">local1</td>
                    <td width="80">CEP1</td>	
                    <td width="100">Não codificada por logradouros</td>	
                    <td width="85">Total do município</td>	

                    </tr>

                    <tr>

                    <td width="100">local2</td>
                    <td width="80">CEP2</td>	
                    <td width="100">Não codificada por logradouros</td>	
                    <td width="85">Total do município</td>	

                    </tr>
                    
                </tbody></table>
            '''
            result, uf_error = self.crawler.search_datas(['AC'])
            self.assertEqual(result, [{'UF': 'AC', 'Localidade': ['local1', 'local2'], 'Faixa de CEP': ['CEP1', 'CEP2']}])
            self.assertEqual(uf_error, [])

    def test_dataframe(self):
        with patch("pandas.concat") as mock_concat:
            mock_concat.return_value = pd.DataFrame({'UF': ['AC'], 'Localidade': ['local1'], 'Faixa de CEP': ['CEP1']})
            df = pd.DataFrame({})
            result = self.crawler.dataframe(df, [{'UF': 'AC', 'Localidade': ['local1'], 'Faixa de CEP': ['CEP1']}])
            self.assertEqual(result.to_dict(), {'UF': {0: 'AC'}, 'Localidade': {0: 'local1'}, 'Faixa de CEP': {0: 'CEP1'}})

if __name__ == '__main__':
    unittest.main()