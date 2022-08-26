from django.contrib import admin
from django.urls import path, include
#from rest_framework.routers import SimpleRouter

from weatherapp.views import index, ForecastAPIView
from rest_framework_simplejwt import views as jwt_views


# router = SimpleRouter()
# router.register('api', ApiScheduleView)
#router.register('api/<int:pk>', ApiScheduleView())


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', index, name='home'),
    path('users/', include('weatherapp.urls')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/forecast_list/', ForecastAPIView.as_view()),
    path('api/forecast_list/<int:pk>/', ForecastAPIView.as_view()),
]

# urlpatterns += router.urls