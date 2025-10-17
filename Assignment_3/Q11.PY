age1=int(input("enter age of person1:"))
price1=float(input("enter the ticket price of person1:"))
if age1<12:
    amt1=price1*0.7
elif age1>59:
    amt1=price1*0.5
else:
    amt1=price1
age2=int(input("enter age of person2:"))
price2=float(input("enter the ticket price of person2:"))
if age2<12:
    amt2=price1*0.7
elif age2>59:
    amt2=price2*0.5
else:
    amt2=price2
age3=int(input("enter age of person3:"))
price3=float(input("enter the ticket price of person3:"))
if age3<12:
    amt3=price3*0.7
elif age3>59:
    amt3=price3*0.5
else:
    amt3=price3
age4=int(input("enter age of person4:"))
price4=float(input("enter the ticket price of person4:"))
if age4<12:
    amt4=price4*0.7
elif age4>59:
    amt4=price4*0.5
else:
    amt4=price4
age5=int(input("enter age of person5:"))
price5=float(input("enter the ticket price of person5:"))
if age5<12:
    amt5=price5*0.7
elif age5>59:
    amt5=price5*0.5
else:
    amt5=price5
total=amt1+amt2+amt3+amt4+amt5
print(f"total ticket amount for all 5 people,{total}")



