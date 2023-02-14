#!/bin/bash 

sudo docker build . --tag linux_commands
sudo docker run -d -p 2226:22 --cap-add=SYS_PTRACE -it linux_commands --read-only

# DEBUG version -- goes into the container automatically
docker_ps=$(sudo docker ps -q | head -n1) 
sudo docker exec -u root -it $docker_ps /bin/bash
