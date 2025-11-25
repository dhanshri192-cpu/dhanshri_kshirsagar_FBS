def armstrongNumber(n):
    temp=n
    sum=0
    while temp>0:
        digit=temp%10
        sum=sum+(digit*digit*digit)
        temp=temp//10
    if sum==n:
            return True
    else:
        return False
n=int(input("enter the number to check armstrong or not:"))
if armstrongNumber(n):
     print(n,"is an armstrong number.")
else:
    print(n,"is not an armstrong number.")

