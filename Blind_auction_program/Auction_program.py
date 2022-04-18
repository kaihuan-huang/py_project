# HINT: You can call clear() to clear the output in the console.
from replit import clear

from art import logo

print(logo)

bids = {}
bidding_finished= False


def find_higest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # bidding_record = {"Justin":111, "Kaihuan": 199}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")


while not bidding_finished:
    name = input('What is your name?: ')
    price = int(input('What is your bid?: $'))
    # Ask name and bid into dictionary as the key and value
    bids[name] = price
    # dictionary key value
    should_continue = input("Are there any other bidders? 'yes' or 'no ' .")
    if should_continue == 'no':
        bidding_finished = True
        find_higest_bidder(bids)
    elif should_continue == 'yes':
        clear()
