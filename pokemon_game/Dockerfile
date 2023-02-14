FROM ubuntu:22.04

RUN apt-get update && apt-get -y install build-essential gcc socat netcat python3 python3-pip
RUN apt-get update -y && DEBIAN_FRONTEND="noninteractive" TZ="America/New_York" apt install openssh-server g++-multilib vim gcc git curl bsdmainutils nano tmux build-essential emacs vim -y

# Setup the users
## Setup the 'pokemon' user to login with
RUN useradd -d /home/pokemon/ -m -p pokemon -s /bin/bash pokemon
RUN echo "pokemon:pokemon" | chpasswd
RUN chown -R root:pokemon  /home/pokemon

WORKDIR /home/pokemon

## Setup the user that owns the flag
RUN useradd -d /home/flag_user/ -m -s /bin/bash flag_user
RUN chown -R root:flag_user  /home/flag_user

RUN pip3 install scrap_engine
COPY ./flag1.txt ./flag1.txt
COPY ./flag2.txt ./flag2.txt
COPY ./flag3.txt ./flag3.txt
COPY ./flag4.txt ./flag4.txt
COPY ./pokete ./pokete
COPY ./run.c ./run.c

RUN gcc /home/pokemon/run.c -o  /home/pokemon/run -ggdb -O0

# Setup the proper file for each set of exercises
RUN chown root:pokemon /home/pokemon/pokete/*
RUN chown root:flag_user /home/pokemon/flag?.txt
RUN chown root:pokemon /home/pokemon/run

# Setup the permissions for the process. Difference between flag_user and pokemon is ability to read the 'flag'
RUN chmod 6755 /home/pokemon/pokete/*
RUN chmod 6755 /home/pokemon/run
RUN chmod 440 /home/pokemon/flag?.txt
RUN chmod 744 /home/pokemon/run.c

# Can't read the contents of the directory but can see inside of the folders, if you know they exist
RUN chmod 773 /tmp/ 

COPY ./bashrc ./.bashrc 
# TODO: /tmp shouldn't be readable but the other things inside it should be - individual folders

# SSH server startup. When launching this, specify which port that the SSH (locally port 22) will be bounded to
RUN mkdir /var/run/sshd
EXPOSE 22/tcp 
ENTRYPOINT service ssh restart && sleep 5d
