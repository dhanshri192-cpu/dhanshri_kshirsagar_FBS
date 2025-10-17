p1=int(input("enter the product1:"))
p2=float(input("enter the product2:"))
p3=float(input("enter the product3:"))
p4=float(input("enter the product4:"))
p5=float(input("enter the product5:"))
total= p1+p2+p3+p4+p5
if total>0:
    gst=total*0.18
    final_amount=total+gst
    print(f"total (without gst): rs.{total}")
    print(f"gst(18%): rs.{gst}")
    print(f"final amount: rs.{final_amount}")
else:
    print("invalid total bill.")