def clinic():
    print "You've just entered the Clinic!"
    print "Is this your first visit?"
    answer = raw_input("Answer with Yes or No:").lower()
    
    if answer == "yes" or answer == "y":
        print "Please fill up this form and get token."
        
    elif answer == "no" or answer == "n":
        print "Show me your token and go inside to visit Doctor."
        
    else:
        print "You didn't answer my question. Sit tight or Answer now."
        clinic()
        
clinic()        
