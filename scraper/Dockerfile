FROM python:3.8
COPY . /scraper

RUN apt-get update
RUN apt-get -y install python3 python3-dev python3-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
RUN pip install --upgrade pip

RUN pip install psycopg2
RUN pip install scrapy
RUN pip install scrapy-playwright

RUN playwright install chromium
RUN playwright install-deps

WORKDIR /scraper