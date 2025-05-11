from django.db import models
from users.models import CustomUser  # Foydalanuvchi bilan bog'lash

class AuctionType(models.Model):
    name = models.CharField(max_length=50)  # English, Dutch, Sealed-bid

    def __str__(self):
        return self.name

class Auction(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    type = models.ForeignKey(AuctionType, on_delete=models.SET_NULL, null=True)
    
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_active = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
class AuctionImage(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='auction_images/')
    alt_text = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.auction.title}"

from simple_history.models import HistoricalRecords

class Auction(models.Model):
    ...
    history = HistoricalRecords()

@property
def winner(self):
    if self.end_time < timezone.now():
        highest_bid = self.bids.order_by('-amount').first()
        return highest_bid.user if highest_bid else None
    return None

