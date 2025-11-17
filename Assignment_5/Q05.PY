amount=int(input("enter the amount:"))
notes=[2000,1000,500,200,100,50,20,10,5,2,1]
note_count={}
for note in notes:
    if amount>=note:
      count =amount//note
      amount=amount%note
      note_count[note]=count
print("minimum number of notes:")
for n in note_count:
   print(f"{n}:{note_count[n]}")