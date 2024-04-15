#!/bin/sh
/app/web/manage.py createcachetable
/app/web/manage.py migrate
/app/web/manage.py collectstatic --no-input
/app/web/manage.py compilemessages