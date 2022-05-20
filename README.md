# ChatBot

Final project for the subject Programming Project, in the field of Computer Science, at the University of Economics in 
Katowice, Semester 2, Part-time studies, Academic year 2021/2022.

## Authors

  * Artur Leśnik
  * Alicja Pęgiel

## About ChatBot

ChatBot is an REST API chat application. The project uses machine learning to teach the bot how to properly communicate 
with humans, while also making sense. 

## Features

  * endpoint for training the spam recognition program
  * endpoint for querying whether the given text is spam
  * endpoint to teach the program new questions and answers
  * endpoint for getting the answer to the question asked
  * endpoint containing information about the project
  * web interface for communication with the chatbot

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
docker build -t chatbot-uekat-gr2-inf-nies ./
docker run --name chatbot-uekat --rm -p 5000:5000 chatbot-uekat-gr2-inf-nies
```

## How to update on production

```commandline
sh deploy-new-version.sh
```

## Swagger API documentation

Below is an endpoint containing the complete swagger documentation of the project's endpoints.

```
http://127.0.0.1:5000/api/doc
```

## Frontend Chat

A special graphic interface for communication with the bot in the form of a web application.

```
http://127.0.0.1:5000/static/chatbot.html
```