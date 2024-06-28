#!/bin/bash

# Ensure pip is available
/usr/bin/python3.9 -m ensurepip --upgrade

# Upgrade pip
/usr/bin/python3.9 -m pip install --upgrade pip

# Install dependencies from requirements.txt
/usr/bin/python3.9 -m pip install -r requirements.txt

# Collect static files
python3.9 manage.py collectstatic --noinput


# Apply database migrations
python3.9 manage.py makemigrations
python3.9 manage.py migrate


