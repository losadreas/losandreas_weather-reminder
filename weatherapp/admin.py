from django.contrib import admin

# Register your models here.
from weatherapp.models import User, Forecast

admin.site.register(User)
admin.site.register(Forecast)