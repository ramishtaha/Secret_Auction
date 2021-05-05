import os

bids = {}


def clear():
    # for windows 
    if os.name == 'nt':
        _ = os.system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')


def add_bidder(name, bid):
    global bids
    bids[name] = bid


def max_bid(all_bids):
    maximum_bid = 0
    max_bidder = ""
    for bidder in all_bids:
        if all_bids[bidder] > maximum_bid:
            maximum_bid = all_bids[bidder]
            max_bidder = bidder
    print(f"The winner is {max_bidder} with a bid of ${maximum_bid}")


print("Welcome to Secret Auction")
from art import logo

print(logo)
choice = "yes"
while choice == "yes":
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    add_bidder(name, price)
    choice = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if choice == "yes":
        clear()

max_bid(bids)
