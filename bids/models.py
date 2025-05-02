from django.db import models
from users.models import CustomUser
from auctions.models import Auction
from django.utils import timezone

class Bid(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name='bids')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    is_auto = models.BooleanField(default=False)
    max_auto_amount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)

    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} - {self.amount} ({'Auto' if self.is_auto else 'Manual'})"
