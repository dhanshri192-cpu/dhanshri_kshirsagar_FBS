
print("please  select option:")
print("a. 1 + 2 + 3 + ... + n")
print("b. 1! + 2! + 3! + ... + n!")
print("c. n^1 + n^2 + n^3 + ... + ")
ch = input("Enter your choice:")


if ch=='a':
      def sumofSeries(n):
         sum=0
         for i in range(1,n+1):
          sum=sum+i
         return sum
      n=int(input("enter the number:"))
      print(sumofSeries(n))

elif ch=='b':
       def factorialNumber(n):
        fact=1
        sum=0
        for i in range(1,n+1):
          fact=fact*i
          sum=sum+fact
        return sum
       n=int(input("enter the number:"))
       print(factorialNumber(n))

elif ch=='c':
       def exponentialNumber(n):
         sum=0
         for i in range(1,n+1):
           sum=sum+(n**i)
         return sum
       n=int(input("enter the number:"))
       print(exponentialNumber(n))
    
else:
      print("exit")




