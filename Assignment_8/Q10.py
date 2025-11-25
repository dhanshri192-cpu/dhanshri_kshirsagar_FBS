def leapYear(year):
   if (year%4==0 and year%100!=0):
      return "leap year"
   else:
      return "not leap year"
n=int(input("enter the year:"))
print(leapYear(n))
      