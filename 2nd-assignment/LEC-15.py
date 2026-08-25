# Program: File Handling Demo

# --- Create a text file and write some content ---
with open("student.txt", "w") as f:
    f.write("Hello, this is the first line.\n")
    f.write("Welcome to Hunarmand Punjab.\n")

print("File created and initial content written.\n")

# --- Read the file content and display ---
with open("student.txt", "r") as f:
    content = f.read()

print("File Content after writing:")
print(content)
print("\n")

# --- Append data to the file ---
with open("student.txt", "a") as f:
    f.write("This line is appended.\n")
    f.write("Python file handling is easy!\n")

print("Data appended successfully.\n")

# --- Read again to show updated content ---
with open("student.txt", "r") as f:
    updated_content = f.read()

print("File Content after appending:")
print(updated_content)
