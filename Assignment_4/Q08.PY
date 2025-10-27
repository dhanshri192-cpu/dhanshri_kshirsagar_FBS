start=int(input("enter the start range:"))
end=int(input("enter end range:"))
for i in range(start,end+1):
    if(i%7==0 and i%5==0):
        print("number is divisible by 7 and multiple of 5 are:",i)