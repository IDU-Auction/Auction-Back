from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('product/<pk>/', login_required(product_detail), name='product-detail'),
]