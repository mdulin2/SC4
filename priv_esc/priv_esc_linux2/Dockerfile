FROM ubuntu:18.04

# Add GDB, Python, SSH, gcc and curl
RUN apt-get update -y && DEBIAN_FRONTEND="noninteractive" TZ="America/New_York" apt install openssh-server g++-multilib vim python git bsdmainutils nano -y



## Setup the 'second_priv' user 
RUN useradd -d /home/second_priv/ -m -p second_priv -s /bin/bash second_priv
RUN echo "second_priv:second_priv" | chpasswd
RUN chown -R root:second_priv  /home/second_priv

#add the flag
ADD ./flag1.txt /home/second_priv/flag.txt

# install sudo 

RUN apt-get -y install sudo


# Give the second_priv user sudo permission w/out password needed to run the 'less' command

RUN echo 'second_priv ALL=(ALL) NOPASSWD: /usr/bin/less' >> \
/etc/sudoers

# Setup the proper file permissions
RUN chown root:second_priv /home/second_priv/flag.txt
RUN chmod 400 /home/second_priv/flag.txt


# SSH server startup. When launching this, specify which port that the SSH (locally port 22) will be bounded to
RUN mkdir /var/run/sshd
EXPOSE 22/tcp 

CMD ["/usr/sbin/sshd", "-D"]
