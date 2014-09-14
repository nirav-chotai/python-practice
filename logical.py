"""Boolean operators aren't just evaluated from left to right. 
Just like with arithmetic operators, 
there's an order of operations for boolean operators:

not is evaluated first;
and is evaluated next;
or is evaluated last.

Parentheses () ensure your expressions are evaluated in the order you want. 
Anything in parentheses is evaluated as its own unit."""

bool_one = False or not True and True
print bool_one

bool_two = False and not True or True
print bool_two

bool_three = True and not (False or False)
print bool_three

bool_four = not not True or False and not True
print bool_four

bool_five = False or not (True and True)
print bool_five

# Use boolean expressions as appropriate on the lines below!

# Make me false!
bool_one = (2 <= 2) and "Alpha" == "Bravo"  # We did this one for you!

# Make me true!
bool_two = 5 == 5 and 7 > 6

# Make me false!
bool_three = 6 < 5 or 5 < 4

# Make me true!
bool_four = "Nirav" == "Chotai" or 4 > 3

# Make me true!
bool_five = "Y" == "Y" and "N" != "C"