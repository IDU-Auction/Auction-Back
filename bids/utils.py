from django.db import transaction
from .models import Bid
from auctions.models import Auction

@transaction.atomic
def place_bid(user, auction, amount, is_auto=False, max_auto_amount=None):
    auction = Auction.objects.select_for_update().get(id=auction.id)

    if not auction.is_active:
        raise Exception("Auction is not active.")

    last_bid = Bid.objects.filter(auction=auction).order_by('-amount').first()

    if last_bid and amount <= last_bid.amount:
        raise Exception("Bid must be higher than the current highest.")

    bid = Bid.objects.create(
        auction=auction,
        user=user,
        amount=amount,
        is_auto=is_auto,
        max_auto_amount=max_auto_amount if is_auto else None,
    )

    update_auto_bidders(auction)
    return bid

def update_auto_bidders(auction):
    auto_bidders = Bid.objects.filter(
        auction=auction,
        is_auto=True
    ).exclude(user=auction.bids.last().user)

    current_max = auction.bids.last().amount

    for auto_bid in auto_bidders:
        if auto_bid.max_auto_amount > current_max:
            new_amount = min(auto_bid.max_auto_amount, current_max + 1)
            Bid.objects.create(
                auction=auction,
                user=auto_bid.user,
                amount=new_amount,
                is_auto=True,
                max_auto_amount=auto_bid.max_auto_amount
            )
            current_max = new_amount
