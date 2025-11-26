list=[[1,4],[3,1],[5,2],[2,3]]
def second(x):
    return x[1]
list.sort(key=second)
print(list)