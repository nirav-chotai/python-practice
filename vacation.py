'''
Created on Aug 4, 2014
Script: Taking a Vacation
@author: nirav.chotai
'''
def hotel_cost(nights):
    #Hotel costs $140 per night
    return 140 * nights

def plane_ride_cost(city):
    if city=="Charlotte":
        return 183
    elif city=="Tampa":
        return 220
    elif city=="Pittsburgh":
        return 222
    elif city=="Los Angeles":
        return 475

def rental_car_cost(days):
    #Every day you rent the car costs $40
    cost = 40 * days
    if days >= 7:
        cost -= 50
    elif days >= 3:
        cost -= 20
    return cost

def trip_cost(city, days, spending_money):
    return hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days) + spending_money

print trip_cost("Los Angeles",5,600)