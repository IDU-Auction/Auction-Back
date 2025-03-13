from django.shortcuts import render, redirect, HttpResponse
from .models import *


def main(request):
    categories = Category.objects.all()
    other = None
    if len(categories) > 12:
        other = categories[12:]
        categories = categories[:12]
    
    context = {
        'categories': categories,
        'other': other
    }

    return render(request, 'index.html', context=context)


def lots(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        products = Product.objects.all().order_by('-end_time')

        context = {
            'products': products,
            'categories': categories
        }

        return render(request, 'lots.html', context=context)


def lots_with_id(request, pk):
    if request.method == 'GET':
        products = Product.objects.filter(category__id=pk)
        categories = Category.objects.all()

        context = {
            'products': products,
            'categories': categories
        }

        return render(request, 'lots.html', context=context)


def categories_product(request, pk):
    category = Category.objects.get(id=pk)
    products = Product.objects.filter(category=category)

    context = {
        'products': products,
    }
    
    return render(request, 'main/product_list.html', context=context)


def lot_detail(request, pk):

    product = Product.objects.filter(pk=pk).first()
    if not product:
        return HttpResponse('400 BAD REQUEST')

    context = {
        'product': product
    }

    return render(request, 'lot.html', context=context)


def sold_product_list(request):
    sold_products = SoldProduct.objects.filter(user=request.user)

    context = {
        'sold_products': sold_products,
    }

    return render(request, )
