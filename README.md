# Crawler Desafio Neoway

crawler to get data from https://www2.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm

clone the project

## RUN WITHOUT DOCKER

export PYTHONPATH="${PYTHONPATH}:${PWD}"

sudo chmod -R 777 src/

python test/test_crawler.py

python src/crawler.py

## RUN WITH DOCKER

sudo docker-compose up --build test_crawler

sudo docker-compose up --build crawler

### RUN DOCKER LOGS
sudo docker-compose up --build -d log-view

you can see the log in http://localhost:9999

# Data Pirates challenge

Welcome to the Data Pirates challenge.


## Scenario

Hello! We have a small adventure to put your skills to the test. In this task you have to collect data from a website and then write the results to a file.


## Requirements

*  Use the https://www2.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm URL;
*  Get data from at least two UFs. The more, the better;
*  Collect all records for each UF;
*  Each record **must** contain **at least** 3 fields: "localidade", "faixa de cep" and a generated "id". Do not let duplicate records in your output file;
*  The output format must be [JSONL](http://jsonlines.org)

## Deliverable

* :heavy_check_mark: The code should be sent through github with at least a README documentation explaining how to test and run it.

* :heavy_check_mark: It would be REALLY nice if it was hosted in a git repo of your **own**. You can create a new empty project, create a branch and Pull Request it to the new master branch you have just created. Provide the PR URL for us so we can discuss the code :grin:. BUT if you'd rather, just compress this directory and send it back to us.

* :x: **Do not** start a Pull Request to this project.

References:

https://www2.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm

http://jsonlines.org

## Pay attention
 * There is no right answer, we will evaluate how you solve problems and what are the results achieved.
 * We work mainly with [Python 3](https://www.python.org) and [Go](https://golang.org/), but feel free to use any language you feel more comfortable with.
 * Unit tests are cool.
 * It's important we can execute your project, so make it clear which steps we need to follow to test and execute your project.