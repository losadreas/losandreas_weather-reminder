from django_celery_beat.models import IntervalSchedule, PeriodicTask
import json


def create_forecast_scheduler_3_hours():
    schedule, created = IntervalSchedule.objects.get_or_create(every=3, period=IntervalSchedule.MINUTES)
    PeriodicTask.objects.create(interval=schedule, name='Repeat 3 hours',
                                task='weatherapp.tasks.send_email',
                                kwargs=json.dumps({'period': 3}))


def create_forecast_scheduler_6_hours():
    schedule, created = IntervalSchedule.objects.get_or_create(every=6, period=IntervalSchedule.MINUTES)
    PeriodicTask.objects.create(interval=schedule, name='Repeat 6 hours',
                                task='weatherapp.tasks.send_email',
                                kwargs=json.dumps({'period': 6}))


def create_forecast_scheduler_12_hours():
    schedule, created = IntervalSchedule.objects.get_or_create(every=12, period=IntervalSchedule.MINUTES)
    PeriodicTask.objects.create(interval=schedule, name='Repeat 12 hours',
                                task='weatherapp.tasks.send_email',
                                kwargs=json.dumps({'period': 12}))


def create_forecast_scheduler_hour():
    schedule, created = IntervalSchedule.objects.get_or_create(every=1, period=IntervalSchedule.MINUTES)
    PeriodicTask.objects.create(interval=schedule, name='Repeat hour',
                                task='weatherapp.tasks.send_email',
                                kwargs=json.dumps({'period': 1}))

