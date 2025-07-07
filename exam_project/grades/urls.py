from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'grades'

urlpatterns = [
    path('', views.index, name='index')
]