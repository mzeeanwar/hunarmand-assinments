# Program: Simple Student Management System

import os

FILE_NAME = "students.txt"

# --- Function to add student ---
def add_student(name, age, grade):
    with open(FILE_NAME, "a") as f:
        f.write(f"{name},{age},{grade}\n")
    print("Student added successfully!")
