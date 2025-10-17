length=int(input("enter the length of wall:"))
breadth=int(input("enter the breadth of wall:"))
cost_per_mtr=int(input("enter the cost per mtr:"))
area=4*(length*breadth)
total_cost=cost_per_mtr*area
print(f"total area,{area}")
print(f"total cost of painting,{total_cost}")