FROM php:8.0-apache

RUN apt-get update

# Add the files
WORKDIR /var/www/html
COPY ./src/html/ ./
RUN chmod 777 ./text

# Make large portions of the code read-only (especially the flag!) 
COPY ./flag.txt /
RUN chmod 444 /flag.txt

EXPOSE 80 


