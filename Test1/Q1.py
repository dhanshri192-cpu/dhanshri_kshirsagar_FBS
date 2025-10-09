length=int(input("enter the length:"))
breadth=int(input("enter the breadth:"))
radius=float(input("enter the radius:"))
area_of_rectangle=length*breadth
area_of_circle=(3.14*radius*radius)/2
perimeter_of_rectangle=(2*length+breadth)
circumference_of_circle=3.14*radius
print(f'area of rectangle is,{area_of_rectangle}')
print(f'area of circle is,{area_of_circle}')
print(f'perimeter of rectangle is,{perimeter_of_rectangle}')
print(f'circumference of circle is,{circumference_of_circle}')