#!/bin/bash
export DJANGO_DEBUG=1
reset
source ./virtual-blog/bin/activate
cd ./django-proj/
python manage.py runserver 0.0.0.0:9000
deactivate

