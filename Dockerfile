FROM python:3
ENV WORKDIR=/opt/demo
ENV DBNAME=inventariodb
ENV DBUSER=invuser
ENV DBPASS=invpass.12
ENV DBHOST=invdb1
ENV DBPORT=5432
WORKDIR $WORKDIR
ADD . $WORKDIR
RUN pip install django psycopg2
RUN chmod 755 /opt/demo/start.sh

EXPOSE 8002

CMD ["/opt/demo/start.sh"]


