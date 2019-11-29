#!/bin/sh

cd /opt/demo
python manage.py migrate
python manage.py runserver 0.0.0.0:8002
