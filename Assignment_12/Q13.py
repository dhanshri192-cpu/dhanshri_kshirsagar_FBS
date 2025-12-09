n=input("enter the string:")
letter=digit=0
for ch in n:
    if ch.isalpha():
        letter+=1
    elif ch.isdigit():
        digit+=1
print("letter is:",letter)
print("digit is:",digit)