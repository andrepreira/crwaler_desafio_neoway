FROM python:3.10-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update
COPY requirements.txt ./
RUN ["pip3", "install", "-r", "requirements.txt"]
ENV PYTHONPATH="${PYTHONPATH}:${PWD}"

COPY src /src
COPY test /test


# RUN ["python3", "-W", "ignore", "crawler.py"]

CMD [ "tail", "-f", "/dev/null" ]