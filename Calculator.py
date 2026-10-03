print("1.Add\n2.Subtract\n3.Multiply\n4.Divide")
ch = input("Enter your choice:")
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
if ch == "1":
    print("Sum is",a+b)
elif ch == "2":
    print("Difference is",a-b)
elif ch == "3":
    print("Product is",a*b)
elif ch == "4":
    print("Divison is",a/b)
else:
    print("Invalid choice")
