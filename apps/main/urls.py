from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('lots/', lots, name='lots'),
    path('lots/<int:pk>/', lots_with_id, name='lots_with_id'),
    path('lots/detail/<int:pk>', lot_detail, name='lot_detail')
    # path('products_list/<pk>/', login_required(categories_product), name='product-list'),
    # path('product/<pk>/', login_required(product_detail), name='product-detail'),
]