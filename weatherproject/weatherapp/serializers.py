from rest_framework.serializers import ModelSerializer
from weatherapp.models import Forecast


class ForecastSerializer(ModelSerializer):
    class Meta:
        model = Forecast
        fields = ['city', 'period']