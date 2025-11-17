n=int(input("enter the employee:"))
total_all=0
for i in range(1,n+1):
    basics=int(input("enter the basics salary:"))
    if (basics<2000):
        da=basics*0.10
        ta=basics*0.12
        hra=basics*0.15
    else:
        da=basics*0.15
        ta=basics*0.18
        hra=basics*0.20
    total=da+ta+hra+basics
    print(f"total salary of employee:{total}")
    total_all=total+1
print(f"total salary of all employee:{total_all}")
