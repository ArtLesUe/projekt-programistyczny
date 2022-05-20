git fetch --all
git pull
docker stop chatbot-uekat
docker image rm chatbot-uekat-gr2-inf-nies
docker build -t chatbot-uekat-gr2-inf-nies ./
docker run -d --name chatbot-uekat --rm -p 5000:5000 chatbot-uekat-gr2-inf-nies
docker logs -f chatbot-uekat
