FROM python:3.9-alpine

MAINTAINER Artur Leśnik <artur.lesnik@edu.uekat.pl>

ADD ./ /app

WORKDIR /app

RUN ["rm", "-r", "-f", "venv"]

RUN ["rm", "-r", "-f", ".git"]

WORKDIR /app/src

RUN ["pip", "install", "--upgrade", "pip"]

RUN ["pip", "install", "flask-restful"]

RUN ["pip", "install", "swagger-ui-py"]

WORKDIR /app

EXPOSE 5000/tcp

CMD ["python", "main.py"]
