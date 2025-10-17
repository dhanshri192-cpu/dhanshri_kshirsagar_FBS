num=int(input("enter the 3-digit number:"))
first=num//100
last=num%10
if(first==last):
    print("the number is palindrome.")
else:
    print("the number is not palindrome.")