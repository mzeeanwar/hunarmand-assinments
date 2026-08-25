# Program: Functions Demo

# --- Function to add two numbers ---
def add_numbers(a, b):
    return a + b

# --- Function to check if a number is prime ---
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# --- Demonstrate default arguments, *args, **kwargs ---
def greet(name="Guest"):
    print(f"Hello, {name}!")

def sum_all(*args):
    return sum(args)

def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# --- Main Execution ---
print("Add Numbers:", add_numbers(10, 5))          # 15
print("Is 17 Prime?", is_prime(17))                # True
print("Is 20 Prime?", is_prime(20))                # False

greet()                                            # Default argument
greet("Shan")                                      # Custom argument

print("Sum of numbers:", sum_all(1, 2, 3, 4, 5))   # 15

show_info(name="Zeeshan Anwar", age=25, city="Gujranwala")     # kwargs demo
