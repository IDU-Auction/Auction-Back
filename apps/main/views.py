from django.shortcuts import render, redirect
from .models import *


def main(request):

    context = {
        'products': Product.objects.all()
    }

    return render(request, 'index.html', context=context)


def product_detail(request, pk):

    product = Product.objects.filter(pk=pk).first()
    if not product:
        return redirect('main')

    context = {
        'product': product
    }

    return render(request, 'product-detail.html', context=context)
