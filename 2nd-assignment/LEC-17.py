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
# --- Catch multiple exceptions ---
try:
    num = int(input("Enter a number: "))
    print("Square of number:", num ** 2)
except ValueError:
    print("Error: Invalid input! Please enter an integer.")
except TypeError:
    print("Error: Type mismatch occurred.")
except Exception as e:
    print("Unexpected Error:", e)
