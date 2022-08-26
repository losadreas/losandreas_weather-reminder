web: gunicorn weatherproject.wsgi
celery: celery -A weatherproject worker -l INFO -P eventlet --beat --scheduler django_celery_beat.schedulers:DatabaseScheduler
