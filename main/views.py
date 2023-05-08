import random

from django.http import HttpResponse
from django.shortcuts import render

from main.models import Product, Category


# Create your views here.
def index(request):
    product_list = Product.objects.all().order_by('?')[:6]
    context = {
        'object_list': product_list,
        'title': 'первые 6 случайных продуктов'
    }
    return render(request, 'main/index.html', context=context)


def products(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Список продуктов'
    }
    return render(request, 'main/products.html', context=context)


def category(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Список категорий'
    }

    return render(request, 'main/category.html', context=context)


def product_detail(request, pk):
    product_item = Product.objects.get(pk=pk),
    context = {
        'object': product_item[0],
        'title': product_item[0].product_name

    }
    return render(request, 'main/product_detail.html', context=context)

# def product_card(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         print(f'User {name} with phone {phone}- send message: {message}')
#     return render(request, 'main/product_detail.html')
