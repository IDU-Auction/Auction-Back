from django.urls import path
from .views import *

urlpatterns = [
    path('login/', sign_in, name='login'),
    path('register/', sign_up, name='register'),
    path('logout/', sign_out, name='logout'),
]