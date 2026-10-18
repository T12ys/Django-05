from django.urls import path

from . import views

app_name = 'quotes'

urlpatterns = [
    path('quote/', views.RandomQuoteView.as_view(), name='random'),
]
