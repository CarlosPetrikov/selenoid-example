# syntax=docker/dockerfile:1

FROM python:3.9-alpine
ENV TZ="America/Sao_Paulo"
ENV LANG C.UTF-8

RUN mkdir /app
WORKDIR /app

RUN apk add --no-cache nano

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . /app
VOLUME /app/config

RUN crontab /app/config/crontab
CMD ["crond", "-f"]
