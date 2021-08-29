from core import models
from core import utils


def send_left_over_token(bid, coin):
    """Send bidder left over token"""
    bid.token_recieved = coin.number_of_available_token
    bid.status = 'recieved some'
    bid.save()

    coin.number_of_available_token = \
        coin.number_of_available_token - coin.number_of_available_token

    coin.save()


def send_complete_token(bid, coin):
    """Send bidder the number of token he bidded for"""
    coin.number_of_available_token = \
        coin.number_of_available_token - bid.number_of_tokens
    coin.save()

    bid.token_recieved = bid.number_of_tokens
    bid.status = 'recieved all'
    bid.save()


def send_bidders_token(bid, coin):
    """Send bidders thier token"""
    if bid.number_of_tokens > \
            coin.number_of_available_token:

        send_left_over_token(bid, coin)

    elif coin.number_of_available_token > bid.number_of_tokens:

        send_complete_token(bid, coin)


def coin_bidders(coin):
    """Get coin bidders"""
    bids = models.Bid.objects.filter(coin=coin.id)\
        .order_by('-bidding_price')
    # number_of_tokens
    for bid in bids:
        send_bidders_token(bid, coin)


def send_tokens():
    """Sends token to bidders"""
    coins = models.Coin.objects.all()
    
    for coin in coins:
        if utils.current_date() == coin.bidding_window \
                and coin.number_of_available_token != 0.0:
            coin_bidders(coin)
