'''
Created on Sep 12, 2014

@author: nirav.chotai
'''
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
for key in prices:
    print key
    print "price: %s" % prices[key]
    print "stock: %s" % stock[key]

total = 0
for key in prices:
    x = prices[key]*stock[key]
    print x
    total = total + x
print total

def compute_bill(food):
    total = 0
    for item in food:
        if (stock[item]>0):
            total = total + prices[item]
            stock[item]=stock[item]-1
    return total

shopping_list = ["banana", "orange", "apple"]
bill = compute_bill(shopping_list)
print bill
print stock
