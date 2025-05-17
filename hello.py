print("enter the mark:")
mark=int(input())
if mark <0 or mark>100:
    print("Invalid mark! Please enter a value between 0 and 100.")
elif mark >= 70:
    print("grade A")
elif mark >=60:
  print("grade B")
elif mark >=50:
    print("grade C")
elif mark >=40:
    print("grade D")
else:
    print("grade E")