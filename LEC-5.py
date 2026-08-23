# Program to swap two variables without using a third variable

# Taking user input
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

print("Before swapping: a =", a, ", b =", b)

# Swapping without third variable
a = a + b
b = a - b
a = a - b

print("After swapping: a =", a, ", b =", b)
