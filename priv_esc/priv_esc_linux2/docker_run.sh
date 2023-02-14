#!/bin/bash 

sudo docker build . --tag linux_priv2
sudo docker run -d --read-only -p 2227:22 --cap-add=SYS_PTRACE -it linux_priv2

# DEBUG version -- goes into the container automatically
docker_ps=$(sudo docker ps -q | head -n1) 
sudo docker exec -u root -it $docker_ps /bin/bash
