FROM ubuntu:18.04

# Add GDB, Python, SSH, gcc and curl
RUN apt-get update && apt-get -y install build-essential gcc socat netcat python3 python3-pip gdb
RUN apt-get update -y && DEBIAN_FRONTEND="noninteractive" TZ="America/New_York" apt install openssh-server g++-multilib vim python git curl bsdmainutils nano tmux perl -y

# Setup the users
## Setup the 'press_me' user to login with
RUN useradd -d /home/press_me/ -m -p press_me -s /bin/bash press_me
RUN echo "press_me:press_me" | chpasswd
RUN chown -R root:press_me  /home/press_me

## Setup the user that owns the flag
RUN useradd -d /home/flag_user/ -m -s /bin/bash flag_user
RUN chown -R root:flag_user  /home/flag_user


# Copy in the files
ADD press_me.c /home/press_me/press_me.c
ADD ./flag.txt /home/press_me/flag.txt

RUN gcc /home/press_me/press_me.c -o  /home/press_me/press_me -ggdb -O0

# Setup the proper file for each set of exercises
RUN chown root:press_me /home/press_me/press_me
RUN chown root:flag_user /home/press_me/flag.txt

# Setup the permissions for the process. Difference between flag_user and press_me is ability to read the 'flag'
RUN chmod 6755 /home/press_me/press_me
RUN chmod 440 /home/press_me/flag.txt
RUN chmod 744 /home/press_me/press_me.c

# SSH server startup. When launching this, specify which port that the SSH (locally port 22) will be bounded to
RUN mkdir /var/run/sshd
EXPOSE 22/tcp 
ENTRYPOINT service ssh restart && sleep 5d

