age=int(input("Enter age:"))
ticket_price=3
if age<=6 or age>=60:
  print("free")
elif age<=18:
  print("ticket price is",ticket_price*0.5)
else:
  print("ticket price is",ticket_price)    