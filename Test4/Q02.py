def factNumber(n):
    if(n==0):
        return 1
    elif(n<0):
        return f'{n} is a negative number.'
    else:
        return n*factNumber(n-1)
n=int(input("enter the number:"))
print(factNumber(n))