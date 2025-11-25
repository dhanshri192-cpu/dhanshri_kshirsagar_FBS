def armStrongnumber(n):
    if(n<=0):
        return 0
    else:
        d=n%10
        return (d**3)+armStrongnumber(n//10)
def checkarmStrongnumber(n):
    if(n==armStrongnumber(n)):
        return f'{n} is armStrongnumber.'
    else:
        return f'{n} is not an armStrongnumber.'
n=int(input("enter the number:"))
print(checkarmStrongnumber(n))
