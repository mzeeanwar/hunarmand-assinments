# Program: Student Dictionary Demo

# --- Create a dictionary for a student ---
student = {
    "name": "Zeeshan Anwar",
    "age": 23,
    "grade": "A"
}

# --- Access values ---
print("Student Name:", student["name"])
print("Student Age:", student["age"])
print("Student Grade:", student["grade"])

# --- Update values ---
student["age"] = 23
student["grade"] = "A+"
print("\nUpdated Student Info:", student)

# --- Loop through dictionary items ---
print("\nLooping through dictionary:")
for key, value in student.items():
    print(key, ":", value)
