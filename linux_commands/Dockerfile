FROM ubuntu:18.04

# Add GDB, Python, SSH, gcc and curl
RUN apt-get update -y && DEBIAN_FRONTEND="noninteractive" TZ="America/New_York" apt install openssh-server vim bsdmainutils -y

# Setup the users
## Setup the 'first_ssh' user 
RUN useradd -d /home/first_ssh/ -m -p first_ssh -s /bin/bash first_ssh
RUN echo "first_ssh:first_ssh" | chpasswd
RUN chown -R root:first_ssh  /home/first_ssh

## Setup the 'deeper' user 
RUN useradd -d /home/deeper/ -m -p deeper -s /bin/bash deeper
RUN echo "deeper:deeper" | chpasswd
RUN chown -R root:deeper  /home/deeper

ADD ./flag1.txt /home/first_ssh/flag.txt

ADD ./flag2.txt /etc/tmp_log

# Setup the proper file for each set of exercises
RUN chown root:first_ssh /home/first_ssh/flag.txt
RUN chmod 440 /home/first_ssh/flag.txt

RUN echo "Grep for the flag in /etc/" > /home/deeper/README.md

# SSH server startup. When launching this, specify which port that the SSH (locally port 22) will be bounded to
RUN mkdir /var/run/sshd
EXPOSE 22/tcp 
ENTRYPOINT service ssh restart && sleep 5d

