
for i in range(0,9):
    for j in range(0,9):
        if(i+j==4 or j-i==4 or i+j==12 or i-j==4):
            print("*",end="  ")
        else:
            print("  ",end="  ")
    print()