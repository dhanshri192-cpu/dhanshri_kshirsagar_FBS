def sumDigit(n):
    sum=0
    while n>0:
        digit=n%10
        n=n//10
        sum=sum+digit
    return sum
n=int(input("enter the number:"))
print("addition of digit=",sumDigit(n))

