n=1
for row in range(10):
    line=[]
    for colunm in range(10):
        line.append(n)
        n=n+1
    if row%2==1:
        line.reverse()
    print(line)
