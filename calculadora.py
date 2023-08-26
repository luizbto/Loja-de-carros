# Function to perform square root
def square_root(x):
    if x < 0:
        return "Error: square root of a negative number"
    else:
        return x ** 0.5

# Main program
print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exponent")
print("6. Square Root")

choice = input("Enter choice(1/2/3/4/5/6): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print(num1, "+", num2, "=", num1 + num2)
elif choice == '2':
    print(num1, "-", num2, "=", num1 - num2)
elif choice == '3':
    print(num1, "*", num2, "=", num1 * num2)
elif choice == '4':
    if num2 == 0:
        print("Error: division by zero")
    else:
        print(num1, "/", num2, "=", num1 / num2)
elif choice == '5':
    print(num1, "^", num2, "=", num1 ** num2)
elif choice == '6':
    if num1 < 0:
        print("Error: square root of a negative number")
    else:
        print("Square root of", num1, "=", square_root(num1))
else:
    print("Invalid input")
