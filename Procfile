release: python manage.py migrate --noinput
web: gunicorn chapa_site.wsgi --bind 0.0.0.0:$PORT
