n=int(input("enter the integer number upto n:"))
for i in range(1,n+1):
    if(i%2!=0 and i%3!=0):
        print("number not divisible by 2 and 3 are:",i)