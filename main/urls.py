from django.urls import path
from .views import *

from main.apps import MainConfig

app_name = MainConfig.name

urlpatterns = [
    path('', index, name="index"),
    path('products/', products, name='products'),
    path('product_card/<int:pk>/', product_card, name='product_card'),
]