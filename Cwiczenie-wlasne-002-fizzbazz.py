for a in range (0, 101):
    
    if (a % 3 == 0 and a % 5 == 0):
        print ("fizz bazz")
        
    elif (a % 3 == 0):
        print ("fizz")
        
    elif (a % 5 == 0):
        print ("bazz")

    else:
        print (a)