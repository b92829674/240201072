num1=int(input("please enter number1:"))
num2=int(input("please enter number2:"))
num3=int(input("please enter number3:"))
if num1<num2 and num1<num3:
  print(num1,"is the minimum")
elif num2<num1 and num2<num3:
  print(num2,"is the minimum")
else:
  print(num3,"is the minimum")    