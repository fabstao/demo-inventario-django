#!/bin/sh

cd /opt/demo
python manage.py migrate
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.filter(email='admin@no.com').delete(); User.objects.create_superuser('admin', 'admin@no.com', 'Password123')"
python manage.py runserver 0.0.0.0:8002
