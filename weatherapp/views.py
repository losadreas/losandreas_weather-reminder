from django.contrib.auth import logout, get_user_model, login
from django.http import Http404
from django.shortcuts import render, redirect
from django.views import View
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from weatherapp.models import Forecast
from django.urls import reverse_lazy
from django.views.generic import CreateView
from weatherapp.forms import CustomUserCreationForm, ForecastForm
from weatherapp.serializers import ForecastSerializer
from weatherapp.utils import *


User = get_user_model()


def index(request):
    # one-time creation PeriodicTasks
    # create_forecast_scheduler_hour()
    # create_forecast_scheduler_3_hours()
    # create_forecast_scheduler_12_hours()
    # create_forecast_scheduler_6_hours()
    return render(request, 'home.html')


class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("forecast_info")
    template_name = "register.html"

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.get(email=request.POST.get("email"))
            login(request, user)
            return redirect('home')
        context = {'form': form}
        return render(request, self.template_name, context)

    def get(self, request, *args, **kwargs):
        logout(request)
        result = super(SignUp, self).get(request, *args, **kwargs)
        return result


class ScheduleAdd(CreateView):
    form_class = ForecastForm
    # success_url = reverse_lazy("home")
    template_name = "forecast_info.html"

    def post(self, request, *args, **kwargs):
        form = ForecastForm(request.POST)
        if form.is_valid():
            forecast, created = Forecast.objects.get_or_create(city=form.cleaned_data['city'], period=form.cleaned_data['period'])
            forecast.user.add(request.user)
            forecast.save()
            return redirect('home')
        else:
            context = {'form': form}
            return render(request, self.template_name, context)

    def get(self, request, *args, **kwargs):
        return super(ScheduleAdd, self).post(request, *args, **kwargs)


class LogOut(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        template = 'logout.html'
        return render(request, template)


class UserView(View):
    def get(self, request, user_id):
        if request.user.id is None:
            return redirect('login')
        template = 'user_view.html'
        user = User.objects.get(id=user_id)
        return render(request, template, {'user_view': user})


class ScheduleView(View):
    def get(self, request, *args, **kwargs):
        if request.user.id is None:
            return redirect('login')
        forecasts = Forecast.objects.filter(user=request.user).all()
        template = "schedule_view.html"
        return render(request, template, {'forecasts': forecasts})


# class ApiScheduleView(ModelViewSet):
#     queryset = Forecast.objects.all()
#     serializer_class = ForecastSerializer
#     permission_classes = [IsAuthenticated]


class ScheduleDelete(View):
    def get(self, request, forecast_id):
        forecast = Forecast.objects.filter(pk=forecast_id).get()
        forecast.user.remove(request.user)
        return redirect('schedules')


class ForecastAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        forecasts = Forecast.objects.filter(user=request.user).all()
        return Response({'forecasts': ForecastSerializer(forecasts, many=True).data})

    def post(self, request):
        serializer = ForecastSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        forecast, created = Forecast.objects.get_or_create(city=request.POST['city'], period=request.POST['period'])
        forecast.user.add(request.user)
        forecast.save()

        return Response({'forecast :': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})
        forecast = Forecast.objects.filter(pk=pk).get()
        forecast.user.remove(request.user)

        return Response({"forecast": "removed from forecast " + str(pk)})