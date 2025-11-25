def power(m,n):
    if(n==0):
        return 1
    else:
        return m**n
m=int(input("enter the m:"))
n=int(input("enter the n:"))
print(power(m,n))