#!/bin/bash 

sudo docker build . --tag pokete
sudo docker run -d -p 22:22 pokete

# DEBUG version -- goes into the container automatically
docker_ps=$(sudo docker ps -q | head -n1) 
sudo docker exec -u root -it $docker_ps /bin/bash
