num=int(input("enter the number:"))
temp=num
sum=0
while temp>0:
    digit=temp%10
    fact=1
    for i in range(1,digit+1):
        fact*=i
    sum+=fact
    temp//=10
if sum==num:
    print(num,"is a strong number.")
else:
    print(num,"is not a strong number.")