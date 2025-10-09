cost_price=int(input("enter the cost price:"))
discount=float(input("enter the discount:"))
discount_amount=(discount/100)*cost_price
selling_price=cost_price-discount_amount
print(f'selling price is,{selling_price}')
