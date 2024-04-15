#!/bin/sh
python3 /app/web/manage.py createcachetable
python3 /app/web/manage.py migrate
python3 /app/web/manage.py collectstatic --no-input
python3 /app/web/manage.py compilemessages