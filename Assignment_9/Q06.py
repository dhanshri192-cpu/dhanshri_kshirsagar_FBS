def fibonacciSeries(n):
        if (n<=1):
            return n
        else:
            return fibonacciSeries(n-1)+fibonacciSeries(n-2)
n=int(input("enter the number:"))
print("fibonacciSeries:")
for i in range(n):
        print(fibonacciSeries(i),end=" ")

