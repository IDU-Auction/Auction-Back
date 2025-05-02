from celery import shared_task
from .models import Auction
from django.utils.timezone import now

@shared_task
def activate_auctions():
    auctions = Auction.objects.filter(is_active=False, start_time__lte=now())
    for auction in auctions:
        auction.is_active = True
        auction.save()

@shared_task
def deactivate_auctions():
    auctions = Auction.objects.filter(is_active=True, end_time__lte=now())
    for auction in auctions:
        auction.is_active = False
        auction.save()
