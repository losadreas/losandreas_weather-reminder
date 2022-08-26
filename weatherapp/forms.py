from django.forms import ModelForm

from .models import User, Forecast
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class ForecastForm(ModelForm):
    class Meta:
        model = Forecast
        fields = ['city', 'period']
