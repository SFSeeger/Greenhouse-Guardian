#!/bin/sh
source /app/base.sh

gunicorn -b 0.0.0.0:80 api.wsgi:application \
    --workers 4 \
    --timeout 120 \
    --log-level warning \
    --access-logfile - \
    --error-logfile -