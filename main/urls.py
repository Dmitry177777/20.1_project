from django.urls import path
from .views import *

from main.apps import MainConfig

app_name = MainConfig.name

urlpatterns = [
    path('', index),
    path('contacts/', contacts),
]