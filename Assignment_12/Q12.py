string=input("enter the string:")
count=0
for ch in string:
    if ch.lower():
        count+=1
print(count)