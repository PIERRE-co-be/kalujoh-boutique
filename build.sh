#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

py manage.py collectstatic --no-input
py manage.py migrate
py manage.py loaddata initial_data.json