import json
import urllib.request
from celery import Celery
from django.core.mail import EmailMessage
from weatherapp.models import Forecast

app = Celery()


@app.task
def send_email(**kwargs):
    forecasts = Forecast.objects.filter(period=kwargs['period']).all()
    city_list = []
    forecast_dict = {}
    for forecast in forecasts:
        city_list.append(forecast.city)
    for city in city_list:
        forecast = Forecast.objects.get(city=city, period=kwargs['period'])
        users = forecast.user.all()
        forecast_dict.update({city:[]})
        for user in users:
            forecast_dict[city].append(user.email)
        url = f'https://api.openweathermap.org/data/2.5/weather?q={urllib.parse.quote(city)}&units=metric&appid=9d95dbbda2a2d0bce2171c4599aabd87'
        sourse = urllib.request.urlopen(url).read()
        list_data = json.loads(sourse)
        temp = list_data['main']['temp']
        temp_min = list_data['main']['temp_min']
        temp_max = list_data['main']['temp_max']
        humidity = list_data['main']['humidity']
        weather = list_data['weather'][0]['description']
        country = list_data['sys']['country']
        message = f'Weather in {city}|{country} temperature: {temp}, humidity: {humidity}, max temperature: {temp_max} ,' \
                  f'mix temperature: {temp_min}, {weather}'
        email = EmailMessage('Forecast subscribe', message, from_email='losandreas-insta@mail.com', to=forecast_dict[city])
        email.send()
