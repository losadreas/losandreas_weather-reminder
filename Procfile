web: gunicorn weatherproject.wsgi
celery: celery -A weatherproject worker --loglevel=INFO -f celery_worker.logs -P eventlet
celery: celery -A weatherproject beat --loglevel=INFO -f celery_beat.logs  --scheduler django_celery_beat.schedulers:DatabaseScheduler