num=int(input("enter the three digit number:"))
d1=num//100
d2=(num//10)%10
d3=num%10
digit_sum=d1+d2+d3
print(f'sum of digit is,{digit_sum}')