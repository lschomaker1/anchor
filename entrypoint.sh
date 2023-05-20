#!/bin/bash
set -e

# Wait for MySQL server to be ready
until mysqladmin ping -h mysql --silent; do
  echo 'Waiting for MySQL server to be up...'
  sleep 1
done

# Run Django server
python manage.py runserver 0.0.0.0:8000
