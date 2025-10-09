interior_cost_of_wall=200
exterior_cost_of_wall=300
area_of_one_wall=4000
interior_wall=int(input("enter the inerior wall:"))
exterior_wall=int(input("enter the exterior wall:"))
area_of_interiorwall=400*8
area_of_exteriorwall=400*7
interior=area_of_interiorwall*200
exterior=area_of_exteriorwall*300
total_cost=interior+exterior
print(f'final cost of wall,{total_cost}')