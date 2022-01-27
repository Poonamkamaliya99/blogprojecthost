web: gunicorn blog.wsgi:application --log-file - --log-level debug
heroku ps:scale web=1

release:python manage.py collectstatic --noinput
release:python manage.py migrate 