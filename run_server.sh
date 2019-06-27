#!/usr/bin/env bash

python manage.py migrate
python manage.py importer
python  runserver 0.0.0.0:$PORT
