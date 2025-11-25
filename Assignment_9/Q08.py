def primeNumber(n,i=2):
    if(n<=1):
        return False
    elif i==n:
        return True 
    elif n%i==0:
        return False
    else:
         return primeNumber(n,i+1)
def checkprimeNumber(n):
    if(primeNumber(n)):
        return f'{n} is a prime number.'
    else:
        return f'{n} is not a prime number.'
n=int(input("enter the number:"))
print(checkprimeNumber(n))