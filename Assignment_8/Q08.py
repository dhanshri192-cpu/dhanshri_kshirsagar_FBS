def reverseNumber(n):
    rev=0
    while n>0:
        digit=n%10
        n=n//10
        rev=rev*10+digit
    return rev
n=int(input("enter the number:"))
print("reverse number =",reverseNumber(n))