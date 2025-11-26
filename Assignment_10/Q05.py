li=[10,20,30,40,50,70]
n=int(input("enter the number:"))
if n in li:
    print("element is present in list.")
    print("times",li.count(n))
else:
    print("element is not present in list.")

