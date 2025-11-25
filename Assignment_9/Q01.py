def sumofSeries(n):
    if(n<=0):
        return 0
    else:
        return n+sumofSeries(n-1)
n=int(input("enter the value:"))
print(sumofSeries(n))