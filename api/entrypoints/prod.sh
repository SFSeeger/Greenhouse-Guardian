#!/bin/sh
source /app/base.sh

gunicorn -b 0.0.0.0:80 api.wsgi:application