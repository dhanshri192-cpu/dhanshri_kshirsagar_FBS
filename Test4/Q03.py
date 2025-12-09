for i in range(1,13):
    for j in range(1,23):
       if(i==1 or i==12):
           print("*", end="  ")
       elif(i+j==15 ):
           print("*",end=" ")
       else:
           print("  ", end="  ")
    print()

    