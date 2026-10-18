from django.urls import path

from . import views

app_name = 'weekday'

urlpatterns = [
    path('weekday/', views.WeekdayView.as_view(), name='today'),
]
