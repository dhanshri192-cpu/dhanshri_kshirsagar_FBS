costprice=int(input("enter the costprice:"))
sellingprice=int(input("enter the sellingprice:"))
if(sellingprice>costprice):
    profit=sellingprice-costprice
    print("it is profit.")
elif(costprice>sellingprice):
    loss=costprice-sellingprice
    print("it is loss.")
else:
    print("no loss,no profit")