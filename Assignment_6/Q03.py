
for i in range(1,5):
    for j in range(5-i,0,-1):
        print( end=' ')
    x=1
    for k in range(1,i+1):
        print(x,end=" ")        
        x=int(x*(i-k)/k)
    print()