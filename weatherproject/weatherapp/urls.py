from django.urls import path, include
from weatherapp.views import SignUp, LogOut, UserView, \
    ScheduleView, ScheduleAdd, ScheduleDelete

urlpatterns = [
    path('logout/', LogOut.as_view(), name='logout'),
    path('<int:user_id>/', UserView.as_view(), name='user_view'),
    path('', include('django.contrib.auth.urls')),
    path('register/', SignUp.as_view(), name='register'),
    path('schedule_add', ScheduleAdd.as_view(), name='schedule_add'),
    path('schedules/', ScheduleView.as_view(), name='schedules'),
    path('schedules_delete/<int:forecast_id>/', ScheduleDelete.as_view(), name='schedule_delete'),
    ]