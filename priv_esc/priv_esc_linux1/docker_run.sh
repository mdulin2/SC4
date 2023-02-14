#!/bin/bash 

sudo docker build . --tag linux_priv1
sudo docker run -d -p 2226:22 --cap-add=SYS_PTRACE --read-only -it linux_priv1

# DEBUG version -- goes into the container automatically
docker_ps=$(sudo docker ps -q | head -n1) 
sudo docker exec -u root -it $docker_ps /bin/bash
