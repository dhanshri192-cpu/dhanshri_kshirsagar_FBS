n=int(input("enter the number:"))
count=0
num=2
while(count<n):
  for i in range(2,num):
       if(num%i==0):
           print(f'{num} is not a prime number.')
           break
  else:
      print(f'{num} is a prime number.')
      count=count+1
  num=num+1
    