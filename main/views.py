import random

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from main.models import Product, Category


# Create your views here.




def index(request):
    product_list = Product.objects.all().order_by('?')[:6]
    context = {
        'object_list': product_list,
        'title': 'первые 6 случайных продуктов'
    }
    return render(request, 'main/index.html', context=context)


class ProductListView(ListView):
    model=Product
    extra_context = {
        'title': 'Список продуктов'
    }

# def products(request):
#     context = {
#         'object_list': Product.objects.all(),
#         'title': 'Список продуктов'
#     }
#     return render(request, 'main/product_list.html', context=context)

class CategoryListView(ListView):
    model=Category
    extra_context = {
        'title': 'Список категорий'
    }

# def category(request):
#     context = {
#         'object_list': Category.objects.all(),
#         'title': 'Список категорий'
#     }
#
#     return render(request, 'main/category_list.html', context=context)


class ProductDetailView(DetailView):
    model=Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data( **kwargs)
        context_data['title'] = context_data['object'].product_name
        return context_data


# def product_detail(request, pk):
#     product_item = Product.objects.get(pk=pk),
#     context = {
#         'object': product_item[0],
#         'title': product_item[0].product_name
#
#     }
#     return render(request, 'main/product_detail.html', context=context)




# def product_card(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         print(f'User {name} with phone {phone}- send message: {message}')
#     return render(request, 'main/product_detail.html')
