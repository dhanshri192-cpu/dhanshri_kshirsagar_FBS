m1=int(input("enter the marks of s1:"))
m2=int(input("enter the marks of s2:"))
m3=int(input("enter the marks of s3:"))
m4=int(input("enter the marks of s4:"))
m5=int(input("enter the marks of s5:"))
total=m1+m2+m3+m4+m5
percentage=total/5
print("total mark:",total)
print("percentage:", percentage)
if percentage>=75:
     print("grade: First class")
elif percentage>=50:
     print("grade: Second class")
elif percentage>=35:
    print("grade: Third class")
else:
    print("grade: Fail")
