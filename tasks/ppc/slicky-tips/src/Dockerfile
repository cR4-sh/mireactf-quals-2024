FROM python:3.9-slim

RUN apt-get update &&  apt -y upgrade 

##next 5 strings install psql 
RUN apt-get install -y lsb-release wget gnupg
RUN sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc |  apt-key add -
RUN apt-get update
RUN apt-get -y install postgresql-13

WORKDIR /app

COPY app /app

RUN pip install --no-cache-dir -r /app/requirements.txt


COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY start_db.sh  /app/start_db.sh


RUN apt-get install -y supervisor

ENV POSTGRES_USER=root
ENV POSTGRES_PASSWORD=root

COPY db/init.sql /docker-entrypoint-initdb.d/database.sql

CMD ["/usr/bin/supervisord"]
