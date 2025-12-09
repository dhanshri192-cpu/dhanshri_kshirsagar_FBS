string=input("enter the string:")
new_string=""
for ch in string:
    if ch==" ":
        new_string+="-"
    else:
        new_string+=ch
print(new_string)