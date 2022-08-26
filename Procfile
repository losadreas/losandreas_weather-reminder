web: gunicorn weatherproject.wsgi
celery_worker: celery -A weatherproject worker -l INFO -P eventlet
celery_beat: celery -A weatherproject beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler