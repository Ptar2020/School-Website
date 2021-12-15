web: python manage.py collectstatic --no-input; gunicorn school.wsgi --log-file - --log-level debug
release:python manage.py migrate