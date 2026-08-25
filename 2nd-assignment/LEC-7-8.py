# Program: Loops and Multiplication Table

# --- Print numbers from 1 to 20 using for loop ---
print("Numbers from 1 to 20:")
for i in range(1, 21):
    print(i, end=" ")
print("\n")  # newline

# --- Print even numbers using while loop ---
print("Even numbers from 2 to 20:")
num = 2
while num <= 20:
    print(num, end=" ")
    num += 2
print("\n")

# --- Nested loop to display multiplication table (1 to 10) ---
print("Multiplication Table (1 to 10):")
for i in range(1, 11):          # outer loop for rows
    for j in range(1, 11):      # inner loop for columns
        print(i * j, end="\t")  # tab spacing
    print()                     # new line after each row
