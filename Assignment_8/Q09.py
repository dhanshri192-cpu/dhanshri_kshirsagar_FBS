def palidromeNumber(n):
    d1=n%10
    n=n//10
    d2=n%10
    n=n//10
    d3=n%10
    n=n//10
    if(d1==d3):
        print("it is palidrome number")
    else:
        print("it is not palidrome number")
n=int(input("enter the number:"))
palidromeNumber(n)