#!/bin/sh

PORT=${PORT:-8000}

python manage.py migrate && \
python manage.py collectstatic --noinput && \
gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT
