feet=int(input("enter the distance in feet:"))
inches=int(input("enter the distance in inches:"))
meter=feet*0.3048+inches*0.0254
centimeter=meter*100
print(f'distance in meter is,{meter}')
print(f'distance in centimeter is, {centimeter}')