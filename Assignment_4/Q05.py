n=int(input("enter the number in terms:"))
a,b=0,1
count=0
print("fibonacci series:")
while count<n:
    print(a,end=" ")
    c=a+b
    a=b
    b=c
    count=count+1