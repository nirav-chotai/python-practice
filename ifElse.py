#Part-1
def using_control_once():
    if (2>1):
        return "Success #1"

def using_control_again():
    if (5==5):
        return "Success #2"

print using_control_once()
print using_control_again()
#Part-2
def greater_less_equal_5(answer):
    if answer>5:
        return 1
    elif answer<5:          
        return -1
    else:
        return 0
        
print greater_less_equal_5(4)
print greater_less_equal_5(5)
print greater_less_equal_5(6)
#Part-3
# Make sure that the_flying_circus() returns True
def the_flying_circus(reply):
    if (reply=='y' or reply=="yes"):    # Start coding here!
        print "You said yesss!"
        # Don't forget to indent
        # the code inside this block!
    elif (reply=='n' or reply=="no"):
        print "You said no...!"
        # Keep going here.
        # You'll want to add the else statement, too!
    else:
        print "You said something else!"

the_flying_circus("no")
the_flying_circus("yes")
the_flying_circus("No")
the_flying_circus("y")
the_flying_circus("n")
the_flying_circus("Yes")
