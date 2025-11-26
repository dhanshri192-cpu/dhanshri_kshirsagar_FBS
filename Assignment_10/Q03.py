def secondMax(li):
    max=li[0]
    smax=0
    for ind in range(0,len(li)):
        if(max<li[ind]):
            smax=max
            max=li[ind]
        elif(max<li[ind]):
            smax=li[ind]
    return max
li=[10,30,60,50,87]
maxele=secondMax(li)
print("second maximum element is",maxele)