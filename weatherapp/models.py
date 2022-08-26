from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class User(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


class Forecast(models.Model):
    PERIOD_CHOICES = ((1, '1'), (3, '3'), (6, '6'), (12, '12'))
    period = models.IntegerField(choices=PERIOD_CHOICES)
    city = models.CharField(max_length=98, blank=True)
    user = models.ManyToManyField(settings.AUTH_USER_MODEL)
