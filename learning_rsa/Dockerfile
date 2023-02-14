FROM ubuntu:22.04

# Add GDB, Python, SSH, gcc and curl
RUN apt-get update -y && apt install -y openssh-server python3 python3-pip
RUN pip install --upgrade pip

WORKDIR /usr/bin

COPY src/runintro_mod.sh .
RUN chmod +x runintro_mod.sh
COPY src/runbabyrsa.sh .
RUN chmod +x runbabyrsa.sh
COPY src/runkidrsa.sh .
RUN chmod +x runkidrsa.sh

WORKDIR /usr/share/learning_rsa

COPY src/requirements.txt .
COPY src/intro_mod.py .
COPY src/babyrsa.py .
COPY src/kidrsa.py .

RUN pip install --no-cache-dir -r requirements.txt

RUN useradd -m -s /usr/bin/runintro_mod.sh -p '' loops1
RUN useradd -m -s /usr/bin/runbabyrsa.sh -p '' loops2
RUN useradd -m -s /usr/bin/runkidrsa.sh -p '' loops3

RUN sed -i '/#PasswordAuthentication yes/c\PasswordAuthentication yes' /etc/ssh/sshd_config
RUN sed -i '/#PermitEmptyPasswords no/c\PermitEmptyPasswords yes' /etc/ssh/sshd_config
RUN sed -i '/UsePAM yes/c\UsePAM no' /etc/ssh/sshd_config

RUN mkdir /var/run/sshd
EXPOSE 22/tcp 
CMD [ "/usr/sbin/sshd", "-D" ]


