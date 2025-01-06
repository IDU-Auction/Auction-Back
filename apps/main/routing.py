from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/prices/<int:product_id>/', consumers.PriceConsumer.as_asgi()),
]
