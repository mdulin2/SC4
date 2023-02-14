FROM ubuntu:18.04

# Add GDB, Python, SSH, gcc and curl
RUN apt-get update -y && DEBIAN_FRONTEND="noninteractive" TZ="America/New_York" apt install openssh-server g++-multilib vim gcc python3 git curl bsdmainutils nano tmux -y python3-pip

# Install 'gef' debugger
RUN apt-get install gdb -y
RUN export LC_CTYPE=C.UTF-8
ENV LC_CTYPE "C.UTF-8" 
RUN bash -c "$(curl -fsSL https://gef.blah.cat/sh)"

# Setup the users
## Setup the 'firsty' user 
RUN useradd -d /home/firsty/ -m -p firsty -s /bin/bash firsty
RUN echo "firsty:firsty" | chpasswd
RUN chown -R root:firsty  /home/firsty

## Setup the 'dead' user 
RUN useradd -d /home/dead/ -m -p dead -s /bin/bash dead
RUN echo "dead:dead" | chpasswd
RUN chown -R root:dead  /home/dead

## Setup the 'auth' user 
RUN useradd -d /home/auth/ -m -p auth -s /bin/bash auth
RUN echo "auth:auth" | chpasswd
RUN chown -R root:auth  /home/auth

# Copy in the files
ADD firsty.c /home/firsty/firsty.c
ADD dead.c /home/dead/dead.c
ADD auth.c /home/auth/auth.c

# Compile the code for these challenges
RUN gcc /home/firsty/firsty.c -o /home/firsty/firsty -O0 -ggdb -m32 -fno-stack-protector -no-pie
RUN gcc /home/dead/dead.c -o /home/dead/dead -O0 -ggdb -m32 -fno-stack-protector -no-pie
RUN gcc /home/auth/auth.c -o /home/auth/auth -O0 -ggdb -m32 -fno-stack-protector -no-pie

ADD ./flag1.txt /home/firsty/flag.txt
ADD ./flag2.txt /home/dead/flag.txt
ADD ./flag3.txt /home/auth/flag.txt

# Setup the proper file for each set of exercises
RUN chown root:firsty /home/firsty/firsty
RUN chown root:firsty /home/firsty/flag.txt
RUN chmod 4755 /home/firsty/firsty
RUN chmod 400 /home/firsty/flag.txt
RUN chmod 744 /home/firsty/firsty.c

RUN chown root:dead /home/dead/dead
RUN chown root:dead /home/dead/flag.txt
RUN chmod 4755 /home/dead/dead
RUN chmod 400 /home/dead/flag.txt
RUN chmod 744 /home/dead/dead.c

RUN chown root:auth /home/auth/auth
RUN chown root:auth /home/auth/flag.txt
RUN chmod 4755  /home/auth/auth
RUN chmod 400 /home/auth/flag.txt
RUN chmod 744 /home/auth/auth.c

# Setup GDB properly for all of the other users
RUN chmod 755 /root/.gef-*
RUN cp /root/.gef-* /home/auth/
RUN cp /root/.gef-* /home/firsty/
RUN cp /root/.gef-* /home/dead/

RUN cp /root/.gdbinit /home/auth/.gdbinit
RUN cp /root/.gdbinit /home/firsty/.gdbinit
RUN cp /root/.gdbinit /home/dead/.gdbinit

# SSH server startup. When launching this, specify which port that the SSH (locally port 22) will be bounded to
RUN mkdir /var/run/sshd
EXPOSE 22/tcp 
ENTRYPOINT service ssh restart && sleep 5d

