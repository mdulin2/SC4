FROM ubuntu:18.04

# Add GDB, Python, SSH, gcc and curl
RUN apt-get update -y && DEBIAN_FRONTEND="noninteractive" TZ="America/New_York" apt install openssh-server g++-multilib vim python git bsdmainutils nano -y



## Setup the 'second_priv' user 
RUN useradd -d /home/third_priv/ -m -p third_priv -s /bin/bash third_priv
RUN echo "third_priv:third_priv" | chpasswd
RUN chown -R root:third_priv  /home/third_priv

#add the flag
ADD ./flag1.txt /home/third_priv/flag.txt

# add a random file that has root permissions

ADD ./reminder.txt /opt/reminder.txt

# install sudo 
RUN apt-get -y install sudo



# Give the second_priv user sudo permission w/out password needed to run the 'less' command

RUN echo 'third_priv ALL=(ALL) NOPASSWD: /usr/bin/vi /opt/reminder.txt' >> \
/etc/sudoers



# Setup the proper file permissions
RUN chown root:third_priv /home/third_priv/flag.txt
RUN chmod 400 /home/third_priv/flag.txt
RUN chown root:third_priv /opt/reminder.txt
RUN chmod 400 /opt/reminder.txt

#RUN echo 'EXPORT PATH=/home/third_priv' > /etc/.profile


# SSH server startup. When launching this, specify which port that the SSH (locally port 22) will be bounded to
RUN mkdir /var/run/sshd
EXPOSE 22/tcp 

CMD ["/usr/sbin/sshd", "-D"]
