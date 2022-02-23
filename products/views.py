from django.shortcuts import render
from products.models import ProductCategory, Product

# функция = контроллер = вьюхи


def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'GeekShop - Каталог',
        'products': Product.objects.all()[:6]
    }
    return render(request, 'products/products.html', context)
