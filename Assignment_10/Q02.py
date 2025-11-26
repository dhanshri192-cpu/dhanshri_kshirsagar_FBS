def minandMax(li):
    min=li[0]
    max=li[0]
    for ind in range(0,len(li)):
        if(min>li[ind]):
            min=li[ind]
        elif(max<li[ind]):
            max=li[ind]
    return min,max
li=[10,20,30,40,50,60]
min_val,max_val=minandMax(li)
print("minimun number:",min_val)
print("maximun element:",max_val)