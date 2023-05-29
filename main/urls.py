from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

from main.apps import MainConfig

app_name = MainConfig.name

urlpatterns = [
    path('', index, name="index"),
    path('products/', ProductListView.as_view(), name='products'),
    path('category/', CategoryListView.as_view(), name='category'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)