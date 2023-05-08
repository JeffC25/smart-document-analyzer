FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive
ENV FLASK_APP=main.py

RUN apt-get update -y
RUN apt-get install python3 python3-pip ipython3 wget -y
RUN apt-get install sqlite3 -y

WORKDIR /news-analyzer

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY Dockerfile .
COPY app/ ./app
COPY .env .
COPY main.py .
ENV FLASK_APP=main.py

CMD flask run --host 0.0.0.0 
