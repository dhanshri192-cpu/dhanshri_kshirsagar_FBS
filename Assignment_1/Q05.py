principal=int(input("enter the pricipal:"))
rate=float(input("enter the rate:"))
time=int(input("enter the time:"))
compound_interest=principal*(1+rate/100)**time-principal
print(f'compound interest is,{compound_interest}')