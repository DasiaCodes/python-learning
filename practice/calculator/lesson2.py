num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Choose operation (+, -, *, /, ** for exponentiation): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
elif operation == "**":
    result = num1 ** num2  # Exponentiation
else:
    result = "Invalid operation"

print("Result:", result)
