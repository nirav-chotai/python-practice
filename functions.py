import math            # Imports the math module
everything = dir(math) # Sets everything to a list of things from math
print everything       # Prints 'em all!

def biggest_number(*args):
    print max(args)
    return max(args)
    
def smallest_number(*args):
    print min(args)
    return min(args)

def distance_from_zero(arg):
    print abs(arg)
    return abs(arg)


biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)

maximum = max(3,7,2,5,8.67,7.68)
print maximum
minimum = min(3,7,2,5,8.67,7.68)
print minimum
absolute = abs(-42)
print absolute

# Print out the types of an integer, a float,
# and a string on separate lines below.

print type(5)
print type(5.5)
print type('a')
print type("Nirav")

def shut_down(s):
    if s=="yes":
        print "Shutting down"
        return "Shutting down"
    elif s=="no":
        print "Shutdown aborted"
        return "Shutdown aborted"
    else:
        print "Sorry"
        return "Sorry"

msg = raw_input('do you really want to shut down?')
shut_down(msg)

def distance_from(x):
    if type(x)==int or type(x)==float:
        print abs(x)
    else:
        return "Nope"
        
distance_from(-5.6)