n=int(input("enter the number:"))
count=0
num=2
while(n>count):
    for i in range(2,num):
        if num%i==0:
            break
    else:
        print(num)
        count=count+1
    num=num+1