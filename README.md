# ChatBot

## Authors
  * Artur Leśnik
  * Alicja Pęgiel

## About ChatBot
ChatBot is an REST API chat application. The project uses machine learning to teach the bot how to properly communicate with humans, while also making sense. 

## Features
TBD

## How to run locally

```commandline
python3 -m venv venv
source venv/bin/activate
pip install flask-restful
pip install swagger-ui-py
pip install gunicorn
gunicorn -w 1 -b 0.0.0.0:5000 main:app
```

## How to run on Docker

```commandline
docker image rm chatbot-uekat-gr2-inf-nies
docker build -t chatbot-uekat-gr2-inf-nies ./
docker run --name chatbot-uekat --rm -p 5000:5000 chatbot-uekat-gr2-inf-nies
```

## Frontend Chat

```
http://127.0.0.1:5000/static/chatbot.html
```