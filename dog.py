
from random import choice

def bark():
    print("woof!")

donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)

total_donations = 0 
for value in donations.values():
    total_donations += value
print(total_donations)

total_donations = sum(donation for donation in donations.values())

total_donations = sum(donations.values())

# This code picks a random food item:

food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!

#DON'T CHANGE THIS DICTIONARY EITHER!
bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

#using IN
if food in bakery_stock:
    print(f"{bakery_stock[food]} left")
else:
    print("We don't make that")

#using get()
quantity = bakery_stock.get(food)
if quantity:
    print(f"{quantity} left")
else:
    print("we don't make that")

    dict = {}

    dict = {["p": "1"]}

print(dict)