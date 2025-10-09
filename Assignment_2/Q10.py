num=int(input("enter the three digit number:"))
d1=num%10
num=num//10
d2=num%10
num=num//10
d3=num%10
num=num//10
reverse=d1*100+d2*10+d3
print(f'reverse is,{reverse}')














