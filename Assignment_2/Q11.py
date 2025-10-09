amount=int(input("enter the amount:"))
notes=[2000,1000,500,200,100,50,20,10]
total_notes=0
for note in notes:
    count=amount // note
    amount=amount%note
    total_notes+=count
print("minimum number of notes required",{total_notes})    
    
