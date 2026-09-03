# Program: Simple Student Management System

import os

FILE_NAME = "students.txt"

# --- Function to add student ---
def add_student(name, age, grade):
    with open(FILE_NAME, "a") as f:
        f.write(f"{name},{age},{grade}\n")
    print("Student added successfully!")
# --- Function to view all students ---
def view_students():
    if not os.path.exists(FILE_NAME):
        print("No student records found.")
        return
    with open(FILE_NAME, "r") as f:
        students = f.readlines()
    print("\nAll Students:")
    for student in students:
        name, age, grade = student.strip().split(",")
        print(f"Name: {name}, Age: {age}, Grade: {grade}")
