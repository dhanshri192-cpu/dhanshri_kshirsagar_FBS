days=int(input("enter the days:"))
years=days//365
days=days%365
weeks=days//7
remaining_days=days%7
print(f'years is',years)
print(f'days is',days)
print(f'weeks is',weeks)
print(f' days are', remaining_days)