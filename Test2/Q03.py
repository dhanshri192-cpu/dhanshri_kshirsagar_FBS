length=50
breadth=40
radius=20
cost_per_mtr=35
s=float(input("enter the number of times fencing to be done(s):"))
perimeter=2*length+breadth+(3.14*radius)
total_wire_length=perimeter*s 
total_cost=cost_per_mtr*total_wire_length
print(f"perimeter of field,{perimeter}meters")
print(f"total wire length,{total_wire_length}meters")
print(f"total cost of fencing, Rs.{total_cost}")