#!/bin/bash 

sudo docker build . --tag ticket-swipey

mkdir -p sessions
sudo docker run -d -p 8199:8199 -v $(pwd)/sessions:/sessions -it ticket-swipey
