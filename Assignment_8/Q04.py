def oddNumber(n):
    for i in range(1,n+1,2):
         if i%2!=0:
           print(i)
n=int(input("enter the number:"))
oddNumber(n)