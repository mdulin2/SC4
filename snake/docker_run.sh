#!/bin/bash 

sudo docker build . --tag snake
sudo docker run -d -p 8083:8083 -p 5000:5000 -it snake

# DEBUG version -- goes into the container automatically
docker_ps=$(sudo docker ps -q | head -n1) 
sudo docker exec -u root -it $docker_ps /bin/bash
