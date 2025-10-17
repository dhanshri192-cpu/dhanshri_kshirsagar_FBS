num=int(input("enter the 3- digit number:"))
first=num//100
second=(num//10)%10
third=num%10
if(first==2*second and first==0.5*third):
    print("yes you have been done.")
else:
    print("please try next.")