FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN apt-get install sqlite3 -y

WORKDIR /news-analyzer

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY Dockerfile .
COPY app/ ./app
COPY instance/ .instance/
COPY .env .
COPY main.py .
ENV FLASK_APP=main.py

CMD flask run --host 0.0.0.0 
