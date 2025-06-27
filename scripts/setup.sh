#!/bin/bash

python -m venv ./virtual-blog
source ./virtual-blog/bin/activate

pip install -r ./requirements.txt
cd ./django-proj/

python3 manage.py makemigrations article
python3 manage.py migrate

python3 manage.py createsuperuser --username=vinicius 
