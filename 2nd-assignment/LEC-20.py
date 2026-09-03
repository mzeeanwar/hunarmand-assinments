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
# --- Function to update student info ---
def update_student(name, new_age, new_grade):
    if not os.path.exists(FILE_NAME):
        print("No student records found.")
        return
    updated = False
    with open(FILE_NAME, "r") as f:
        students = f.readlines()
    with open(FILE_NAME, "w") as f:
        for student in students:
            s_name, s_age, s_grade = student.strip().split(",")
            if s_name == name:
                f.write(f"{name},{new_age},{new_grade}\n")
                updated = True
            else:
                f.write(student)
    if updated:
        print("Student updated successfully!")
    else:
        print("Student not found.")
# --- Function to delete student ---
def delete_student(name):
    if not os.path.exists(FILE_NAME):
        print("No student records found.")
        return
    deleted = False
    with open(FILE_NAME, "r") as f:
        students = f.readlines()
    with open(FILE_NAME, "w") as f:
        for student in students:
            s_name, s_age, s_grade = student.strip().split(",")
            if s_name == name:
                deleted = True
                continue
            f.write(student)
    if deleted:
        print("Student deleted successfully!")
    else:
        print("Student not found.")
# --- Bonus: OOP Student Class ---
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"
# --- Menu-driven program ---
def menu():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Update Student Info")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            age = input("Enter age: ")
            grade = input("Enter grade: ")
            add_student(name, age, grade)
        elif choice == "2":
            view_students()
        elif choice == "3":
            name = input("Enter name to update: ")
            new_age = input("Enter new age: ")
            new_grade = input("Enter new grade: ")
            update_student(name, new_age, new_grade)
        elif choice == "4":
            name = input("Enter name to delete: ")
            delete_student(name)
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")

# --- Run the program ---
menu()
