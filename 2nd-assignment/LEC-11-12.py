# Program: Lists, Tuples, and Sets

# --- Create a list of 5 items and print each item ---
items = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
print("List items:")
for item in items:
    print(item)

print("\n")

# --- Create a tuple and demonstrate immutability ---
my_tuple = (10, 20, 30, 40, 50)
print("Tuple items:", my_tuple)

# Trying to change a tuple element will cause an error
# Uncommenting the next line will raise: TypeError
# my_tuple[0] = 99

print("Tuples are immutable, so elements cannot be changed.\n")

# --- Create a set and perform union, intersection, and difference ---
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print("Set A:", set_a)
print("Set B:", set_b)

print("Union:", set_a | set_b)            # or set_a.union(set_b)
print("Intersection:", set_a & set_b)     # or set_a.intersection(set_b)
print("Difference (A - B):", set_a - set_b)  # or set_a.difference(set_b)
