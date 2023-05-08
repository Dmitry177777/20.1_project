from django.urls import path
from .views import *

from main.apps import MainConfig

app_name = MainConfig.name

urlpatterns = [
    path('', index, name="index"),
    path('products/', products, name='products'),
    path('category/', category, name='category'),
    path('product_detail/<int:pk>/', product_detail, name='product_detail'),
]