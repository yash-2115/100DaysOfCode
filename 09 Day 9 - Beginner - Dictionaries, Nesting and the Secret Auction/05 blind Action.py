from replit import clear
from art import logo

print(logo)

data ={}
bidding_stop = False

def find_highest_bidder(bidding_record):
    highest_bid = 0

    for bidder in bidding_record:
        bid_ammount = bidding_record[bidder]
        if bid_ammount > highest_bid:
            highest_bid = bid_ammount
            winner = bidder
        print(f"The winner is {winner} with bid of ${highest_bid}")

while not bidding_stop:
    name = str(input("What is your name: "))
    bid_price = int(input("Please enter bid price: $"))
    data[name] = bid_price
    ask = str(input("Are there any other bidders? Type 'yes' or 'no'.\n"))

    if ask == "no":
        bidding_stop = True
        find_highest_bidder(data)
    elif ask == "yes":
        clear()