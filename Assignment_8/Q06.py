def fibonacciSeries(n):
    a=1
    b=1
    for i in range(n):
       print(a,end=" ")
       a,b=b, a+b
n=int(input("enter number of terms:"))
fibonacciSeries(n)