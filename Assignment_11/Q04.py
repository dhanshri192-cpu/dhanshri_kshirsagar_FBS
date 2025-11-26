def number(li):
    for i in range(len(li)):
        for j in range(0,len(li)-i-1):
            if(li[j]>li[j+1]):
                li[j],li[j+1]=li[j+1],li[j]
    return li[-2]
li=[10,20,30,40,50,60,70]
print(number(li))