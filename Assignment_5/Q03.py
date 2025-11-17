n=int(input("how many passengers?"))
cost=float(input("enter cost per ticket:"))
total=0
for i in range(n):
    age=int(input("enter age:"))
    if age<12:
        amount=cost*0.3
    elif age>59:
        amount=cost*0.5
    else:
        amount=cost
    total=total+amount
print("total amount to pay= ",total)