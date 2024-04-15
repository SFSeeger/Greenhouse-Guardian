source base.sh

python -Xfrozen_modules=off -m debugpy --listen 0.0.0.0:3000 /app/web/manage.py runserver 0.0.0.0:80