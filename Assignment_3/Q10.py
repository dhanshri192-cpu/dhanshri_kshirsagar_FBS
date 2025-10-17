gender=input("enter the gender (male/female):")
age=int(input("enter the age male and female:"))
if (gender=='male' and age>=21):
    print(" eligible for marriage..")
elif(gender=='female' and age>=18):
    print("eligible for marriage..")
else:
    print("not eligible for marriage..")