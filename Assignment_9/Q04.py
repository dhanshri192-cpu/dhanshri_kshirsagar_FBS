def sumofNumber(n):
    if(n<=0):
        return 0
    else:
        return n+sumofNumber(n-1)
n=int(input("enter the number:"))
print(sumofNumber(n))