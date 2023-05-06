FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y
RUN apt-get install python3 python3-pip ipython3 wget -y
RUN apt-get install sqlite3 -y

WORKDIR /news-analyzer-JeffC25

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT [ ""]