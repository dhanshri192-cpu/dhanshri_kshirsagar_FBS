ch=''
while ch!='f':
    print("please  select option:")
    print("a. 1! + 2! + 3! + ... + n!")
    print("b. n^1 + n^2 + n^3 + ... + ")
    print("c. Geometric series (a, r, n)")
    print("d. a + a^2/2 + a^3/3 + ... + a^10/10")
    print("e. x - x^2/3 + x^3/5 - x^4/7 + ... up to n terms")
    print("f.Exit")
    ch = input("Enter your choice:")

    if ch == 'a':
        n = int(input("Enter value of n: "))
        sum=0
        fact=1
        for i in range(1,n+1):
                fact=fact*i
                sum=sum+fact
        print("Sum of series =", sum)

    elif ch == 'b':
        n = int(input("Enter value of n: "))
        sum=0
        for i in range(1,n+1):
                sum=sum+(i**i)
        print("Sum of series =",sum)

    elif ch == 'c':
        a = float(input("Enter first term (a): "))
        r = float(input("Enter common ratio (r): "))
        n = int(input("Enter number of terms (n): "))
        sum=a*(r**n-1)//(r-1)
        print("Sum of geometric series =",sum)

    elif ch == 'd':
        a = float(input("Enter value of a: "))
        sum=0               
        for i in range(1,11):
             sum=sum+(a**i)/i
        print("Sum of series =", sum)

    elif ch== 'e':
        x = float(input("Enter value of x: "))
        n = int(input("Enter number of terms: "))
        for i in range(1,n+1):
             num=x*(i+1)
             d=2*i+1
             sum=sum *(num/d)
             sign=-1
        print("Sum of series =", sum)

    else:
        print("Exiting program Thank you!")

