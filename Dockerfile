FROM python:3
ENV WORKDIR=/opt/demo
ENV DBNAME=inventariodb
ENV DBUSER=invuser
ENV DBPASS=invpass.12
ENV DBHOST=invdb1
ENV DBPORT=5432
ADD . $WORKDIR
RUN pip -y install django psycopg2

EXPOSE 8002


