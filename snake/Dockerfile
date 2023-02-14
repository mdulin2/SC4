FROM ubuntu:22.04
ENV PYTHONUNBUFFERED 1
RUN apt-get update 
RUN apt-get install -y python3 python3-pip vim tmux

RUN pip3 install gunicorn Flask-WTF Flask-Cors

RUN mkdir /code
WORKDIR /code
COPY ./backend ./backend/
COPY ./frontend ./frontend/
COPY ./startup.sh ./startup.sh

# Start the service
CMD ./startup.sh
