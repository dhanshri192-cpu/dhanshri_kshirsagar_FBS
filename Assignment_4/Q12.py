start=int(input("enter the starting number:"))
end=int(input("enter the ending nunmer:"))
print("armstrong number between ",start,"and", end,"are:")
for n in range(start, end+1):
    digit=str(n)
    power=len(digit)
    total=0
    for d in digit:
        total+=int(d)**power
    if total==n:
        print(n)