FROM ubuntu:18.04

# Add GDB, Python, SSH, gcc and curl
RUN apt-get update -y && DEBIAN_FRONTEND="noninteractive" TZ="America/New_York" apt install vim gcc curl tmux g++-multilib -y

## Setup the 'time' user 
RUN useradd -d /home/time/ -m -p time -s /bin/bash time

# Copy in the files
ADD server.c /home/time/server.c

# Compile the code for these challenges
RUN gcc /home/time/server.c -o /home/time/server -O0 -ggdb -m32 -fno-stack-protector -no-pie

# SSH server startup. When launching this, specify which port that the SSH (locally port 22) will be bounded to
ENTRYPOINT /home/time/server 10000

