web: gunicorn weatherproject.wsgi
celery_worker: celery -A weatherproject worker --loglevel=INFO -f celery_worker.logs -P eventlet
celery_beat: celery -A weatherproject beat --loglevel=INFO -f celery_beat.logs  --scheduler django_celery_beat.schedulers:DatabaseScheduler