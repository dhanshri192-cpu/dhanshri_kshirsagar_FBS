start=int(input("enter the start range:"))
end=int(input("enter the end range:"))
num=int(input("enter the number check divisibility:"))
for i in range(start,end+1):
    if(i%num==0):
        print(f"number is divisible by {num} are:",i, end=" ")