FROM python:3.10.10-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH="${PYTHONPATH}:${PWD}"

RUN apt-get update
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY src /src
COPY test /test
