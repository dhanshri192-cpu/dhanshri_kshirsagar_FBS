li=[10,23,34,4,5,67,78,90,20,21]
m=int(input("enter the value of m:"))
n=int(input("enter the value of n:"))
result= list(filter(lambda x :x%m==0 and x%n==0,li))
print(result)