a = int(input("Enter the dimensions of first side"))
b = int(input("Enter the dimensions of second side"))
c = int(input("Enter the dimensions of third side"))
if a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or c ** 2 + b ** 2 ==a ** 2 :
    print("Right angled triangle")
else :
    print("Not a right angled triangle")
