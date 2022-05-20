# ChatBot
## Authors
Artur Leśnik i Alicja Pęgiel
## About ChatBot
ChatBot is an REST API chat application. The project uses machine learning to teach the bot how to properly communicate with humans, while also making sense. 
## Features
TBD

## How to install

```
pip install flask-restful
pip install swagger-ui-py
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