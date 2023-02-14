#!/bin/bash 

sudo docker build . --tag facial_recognition
sudo docker run -d -p 8082:8082 -it facial_recognition

# DEBUG version -- goes into the container automatically
docker_ps=$(sudo docker ps -q | head -n1) 
sudo docker exec -u root -it $docker_ps /bin/bash
