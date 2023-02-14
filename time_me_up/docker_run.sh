#!/bin/bash 

sudo docker build . --tag time_me_up
sudo docker run -d -p 10000:10000 --cap-add=SYS_PTRACE --security-opt seccomp=unconfined -it time_me_up

# DEBUG version -- goes into the container automatically
docker_ps=$(sudo docker ps -q | head -n1) 
sudo docker exec -u root -it $docker_ps /bin/bash
