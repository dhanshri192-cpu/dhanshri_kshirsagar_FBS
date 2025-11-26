n=[10,22,30,45,57,60]
even=[]
odd=[]
for i in n:
     if i%2==0:
          even.append(i)
     else:
          odd.append(i)
print("even:",even)
print("odd:",odd)