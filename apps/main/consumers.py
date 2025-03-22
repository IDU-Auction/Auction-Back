import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Price, Product
from asgiref.sync import sync_to_async

from apps.authentication.models import CustomUser

class PriceConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.product_id = self.scope['url_route']['kwargs']['product_id']
        self.group_name = f'prices_{self.product_id}'

        # Join room group
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        """
        Handle incoming messages from WebSocket clients.
        """
        data = json.loads(text_data)
        user_id = data.get('user_id')
        price_value = data.get('price')

        if user_id and price_value:
            # Save the new price and get the updated price list
            prices = await self.save_price(user_id, price_value)
            
            # Send updated price list to all clients
            await self.channel_layer.group_send(
                self.group_name,
                {
                    'type': 'price_list_update',
                    'prices': prices,
                }
            )

    @sync_to_async
    def save_price(self, user_id, price_value):
        """
        Save the new price and return the updated list of prices.
        """
        user = CustomUser.objects.get(id=user_id)
        product = Product.objects.get(id=self.product_id)
        
        # Create a new Price instance
        last_price = Price.objects.filter(product=product).last()
        if last_price:
            last_price = last_price.price
        else:
            last_price = product.initial_price

        if int(price_value) > last_price:
            Price.objects.create(product=product, user=user, price=price_value)

        # Fetch updated list of prices for the product
        prices = Price.objects.filter(product=product).order_by('-date').values(
            'user__phone_number', 'price'
        )
        print(prices)
        return list(prices)

    async def price_list_update(self, event):
        """
        Send the updated price list to the client.
        """
        await self.send(text_data=json.dumps({
            'prices': event['prices'],
        }))
