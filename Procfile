web: gunicorn weatherproject.wsgi
celery: celery -A weatherproject worker -P eventlet --beat --loglevel=info
