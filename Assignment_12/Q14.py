str=input("enter the string:")
words=str.split()
checked=[]
for w in words:
    if w not in checked:
        count=0
        for word in words:
            if word==w:
                count+=1
        print(w,":",count)
        checked.append(w)
        
  