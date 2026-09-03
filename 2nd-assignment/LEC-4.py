# Program: Operators Demo

# --- Arithmetic Operators ---
a = 15
b = 4
print("Arithmetic Operators:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
print("Floor Division:", a // b)

print("\n")

# --- Comparison Operators ---
x = 10
y = 20
print("Comparison Operators:")
print("x == y:", x == y)
print("x != y:", x != y)
print("x > y:", x > y)
print("x < y:", x < y)
print("x >= 10:", x >= 10)
print("y <= 20:", y <= 20)

print("\n")

# --- Logical Operators ---
p = True
q = False
print("Logical Operators:")
print("p and q:", p and q)
print("p or q:", p or q)
print("not p:", not p)

print("\n")

# --- Assignment Operators ---
num = 5
print("Assignment Operators:")
num += 3   # num = num + 3
print("After += 3:", num)
num -= 2   # num = num - 2
print("After -= 2:", num)
num *= 4   # num = num * 4
print("After *= 4:", num)
num /= 6   # num = num / 6
print("After /= 6:", num)
num %= 3   # num = num % 3
print("After %= 3:", num)

print("\n")

# --- Bitwise Operators ---
a = 6   # binary: 110
b = 3   # binary: 011
print("Bitwise Operators:")
print("a & b:", a & b)   # AND
print("a | b:", a | b)   # OR
print("a ^ b:", a ^ b)   # XOR
print("~a:", ~a)         # NOT
print("a << 1:", a << 1) # Left shift
print("a >> 1:", a >> 1) # Right shift

print("\n")

# --- Expression with Multiple Operators ---
result = (10 + 5) * 2 > 20 and (4 | 1) == 5
print("Expression with multiple operators result:", result)
