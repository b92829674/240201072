GPA=float(input("Enter your GPA:"))
number_of_lectures=int(input("Enter number of lectures:"))
if GPA<2.0:
  if number_of_lectures<47:
    print("not enough number of lectures and GPA ")
  else:
    print("not enough GPA")
else:
  if number_of_lectures<47:      
    print("not enough number of lectures")
  else:
    print("GRADUATED!")  