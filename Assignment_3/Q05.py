a=int(input("enter the side1:"))
b=int(input("enter the side2:"))
c=int(input("enter the side3:"))
if(a==b==c):
    print("the triangle is equilateral..")
elif(a==b or b==c or c==a):
    print("the triangle is isosceles.")
else:
    print("the triangle is scalene.")
