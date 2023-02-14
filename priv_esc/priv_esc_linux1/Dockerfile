FROM ubuntu:18.04

# Add GDB, Python, SSH, gcc and curl
RUN apt-get update -y && DEBIAN_FRONTEND="noninteractive" TZ="America/New_York" apt install openssh-server g++-multilib vim python git bsdmainutils nano -y


## Setup the 'first_ssh' user 
RUN useradd -d /home/first_priv/ -m -p first_priv -s /bin/bash first_priv
RUN echo "first_priv:first_priv" | chpasswd
RUN chown -R root:first_priv  /home/first_priv

#add the flag
ADD ./flag1.txt /home/first_priv/flag.txt

# install sudo 
RUN apt-get -y install sudo


# add the 'first_priv' user to the sudoers group

RUN usermod -aG sudo first_priv

# Setup the proper file permissions
RUN chown root:first_priv /home/first_priv/flag.txt
RUN chmod 400 /home/first_priv/flag.txt


# SSH server startup. When launching this, specify which port that the SSH (locally port 22) will be bounded to
RUN mkdir /var/run/sshd
EXPOSE 22/tcp 

CMD ["/usr/sbin/sshd", "-D"]
