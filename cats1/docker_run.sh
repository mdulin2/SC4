#!/bin/bash 

sudo docker build . --tag cats
sudo docker run -d -p 80:80 --cap-add=SYS_PTRACE -it cats

# DEBUG version -- goes into the container automatically
docker_ps=$(sudo docker ps -q | head -n1) 
sudo docker exec -u root -it $docker_ps /bin/bash
