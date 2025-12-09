str1=input("enter the string:")
str2=input("enter the string:")
len1=0
for ch in str1:
    len1+=1
len2=0
for ch in str2:
    len2+=1
if len1>len2:
    print(str1)
elif len2>len1:
    print(str2)
else:
    print("both string are equal in length")