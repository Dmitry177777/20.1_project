from django.http import HttpResponse
from django.shortcuts import render

from main.models import Product


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def products(request):
   context={
       'object_list': Product.objects.all()
   }

   return render(request, 'main/products.html', context=context)


def product_card(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'User {name} with phone {phone}- send message: {message}')
    return render(request, 'main/product_card.html')
