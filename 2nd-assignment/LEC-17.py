# Program: Exception Handling Demo

# --- Handle division by zero using try/except ---
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")

print("\n")
