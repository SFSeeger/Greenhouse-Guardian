#!/bin/sh

/app/web/manage.py createcachetable
/app/web/manage.py migrate
/app/web/manage.py collectstatic --no-input
/app/web/manage.py compilemessages

python -Xfrozen_modules=off -m debugpy --listen 0.0.0.0:3000 /app/web/manage.py runserver 0.0.0.0:80