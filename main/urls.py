from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

from main.apps import MainConfig

app_name = MainConfig.name

urlpatterns = [
    path('', index, name="index"),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('product_item/<int:pk>/', ProductDetailView.as_view(), name='product_item'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('products/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),

]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)