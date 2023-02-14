FROM ubuntu:22.04
ENV PYTHONUNBUFFERED 1
RUN apt-get update 
RUN apt-get install -y python3 python3-pip cmake

RUN pip3 install gunicorn Flask-WTF face_recognition Flask 

COPY ./src/ /code
WORKDIR /code

# Start the service
CMD gunicorn server:app --bind 0.0.0.0:8082

