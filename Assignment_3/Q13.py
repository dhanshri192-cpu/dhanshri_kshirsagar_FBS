units=75
amt=0
units=int(input("enter the units of bills:"))
if(units>0):
    if(units>50):
        if(units>150):
            if(units>250):
                pass
            else:
                amt=50*0.5+100*0.75+(units-150)*1.2
        else:
            amt=50*0.5*+(units-50)*0.75
    else:
        amt=units*0.5
else:
    amt=0
print(amt)