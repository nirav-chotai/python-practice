"""
     Boolean Operators
---------------------------
True and True is True
True and False is False
False and True is False
False and False is False

True or True is True
True or False is True
False or True is True
False or False is False

Not True is False
Not False is True

"""
bool_one = 3 < 2 and 5 == 6
print bool_one

bool_two = -(-(-(-2))) == -2 and 4 >= 16**0.5
print bool_two

bool_three = 19 % 4 != 300 / 10 / 10 and 7 > 8
print bool_three

bool_four = -(1**2) < 2**0 and 10 % 10 <= 20 - 10 * 2
print bool_four

bool_five = 2 != 3 and 5 > 4
print bool_five

#We can replace and with or, then results will be changed based on above table.

bool_one = 2**3 == 108 % 100 or 'Cleese' == 'King Arthur'
print bool_one

bool_two = 4 < 5 or 5< 4
print bool_two

bool_three = 100**0.5 >= 50 or 3 >= 4
print bool_three

bool_four = 5 == 5 or 6 < 7 
print bool_four

bool_five = 1**100 == 100**1 or 3 * 2 * 1 != 3 + 2 + 1
print bool_five
