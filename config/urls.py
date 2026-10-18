from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.hello.urls')),
    path('', include('apps.weekday.urls')),
    path('', include('apps.quotes.urls')),
]
