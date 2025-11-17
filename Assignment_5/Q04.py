num=int(input("enter the number:"))
temp=num
sum=0
while temp>0:
    digit=temp%10
    temp=temp//10
    sum=sum+(digit*digit*digit)
    
if(num==sum):
    print(num,"is an armstrong number.")
else:
    print(num,"is not an armstrong number.")