# Function for add
def add(a, b):
    return a + b

# Function for subtract
def subtract(a, b):
    return a - b

# Function for multiply
def multiply(a, b):
    return a * b

# Function for divide
def divide(a, b):
    return a / b

#function for modulus
def modulus(a, b):
    return a % b

#CLI for calculator
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Modulus")
print("6.Exit")
choice = input("Enter choice(1/2/3/4/5/6):")
if choice == '1':
    print("Enter two numbers:")
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))
    print(a, "+", b, "=", add(a, b))
elif choice == '2':
    print("Enter two numbers:")
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))
    print(a, "-", b, "=", subtract(a, b))
elif choice == '3':
    print("Enter two numbers:")
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))
    print(a, "*", b, "=", multiply(a, b))
elif choice == '4':
    print("Enter two numbers:")
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))
    print(a, "/", b, "=", divide(a, b))
elif choice == '5':
    print("Enter two numbers:")
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))
    print(a, "%", b, "=", modulus(a, b))
elif choice == '6':
    print("Bye!")
    exit()
else:
    print("Invalid input")
    exit()

