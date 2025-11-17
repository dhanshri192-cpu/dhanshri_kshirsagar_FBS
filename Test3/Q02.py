n=int(input("enter the value of n:"))
sum=0
fact=1
for i in range(1,n+1):
    fact=fact*i
    term=1/fact
    sum=sum+term
print("sum of series=",sum)