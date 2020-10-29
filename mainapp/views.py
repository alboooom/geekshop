from django.shortcuts import render
from . import models

from django.http import HttpResponse
# Create your views here.


def main(request):
    data = {
        'products': models.Products.objects.all(),
        'categories': models.Category.objects.all()
    }
    return render(request, 'mainapp/index.html', {'data': data})


def products(request):
    data = {
        'products': models.Products.objects
    }
    return render(request, 'mainapp/product.html', {'ds': data})


def contact(request):
    return render(request, 'mainapp/contact.html')
