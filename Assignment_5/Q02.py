students=int(input("enter the numbers of students:"))
total_percentage=0
for i in range(1,1+students):
    print(f"enter the marks of 5 subject of students {i}:")
    total_marks=0
    for j in range(1,6):
        marks=float(input(f"enter the subjects {j} marks:"))
        total_marks+=marks
    percentage=total_marks/5
    total_percentage+=percentage
    if percentage>=75:
        grade="distinction"
    elif percentage>=60:
        grade="first class"
    elif percentage>=50:
        grade="second class"
    elif percentage>=35:
        grade="pass"
    else:
        grade="fail"
    print(f"total marks: {total_marks}")
    print(f"percentage:{percentage}")
    print(f"grade:{grade}")
average=total_percentage/students
print(f"average percentage of all students is {average}")