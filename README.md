# Python-And-Bash
Task 1: Grade Checker
Objective

Take a score as input and print the grade using basic if-else conditions.

Grading Criteria

90 and above : A
80 to 89 : B
70 to 79 : C
60 to 69 : D
Below 60 : F

Code

score = int(input("Enter your score: "))

if score >= 90:
print("Grade: A")
elif score >= 80:
print("Grade: B")
elif score >= 70:
print("Grade: C")
elif score >= 60:
print("Grade: D")
else:
print("Grade: F")

Command to Run

python grade_checker.py

Explanation

The program takes marks as input, converts them into an integer, and uses if-else statements to determine and display the grade.

Task 2: Student Grades Management
Objective

Create a dictionary to store student names and their grades. The program allows adding new students, updating existing grades, and viewing all student records.

Code

students = {}

while True:
print("1. Add Student")
print("2. Update Student Grade")
print("3. View All Students")
print("4. Exit")

choice = input("Enter your choice: ")

if choice == "1":
    name = input("Enter student name: ")
    grade = input("Enter grade: ")
    students[name] = grade
    print("Student added successfully.")

elif choice == "2":
    name = input("Enter student name: ")
    if name in students:
        grade = input("Enter new grade: ")
        students[name] = grade
        print("Grade updated successfully.")
    else:
        print("Student not found.")

elif choice == "3":
    for name, grade in students.items():
        print(name, ":", grade)

elif choice == "4":
    break

else:
    print("Invalid choice")

Command to Run

python student_grades.py

Explanation

A dictionary is used to store student data. The program runs continuously and performs actions based on user input using conditional statements.

Task 3: Write to a File
Objective

Create a text file and write content into it using Python file handling.

Code

file = open("sample.txt", "w")
file.write("Hello, this is a sample file.\nWelcome to Python file handling.")
file.close()

print("Data written to file successfully.")

Command to Run

python write_file.py

Explanation

The file is opened in write mode, content is written using the write() function, and the file is closed to save changes.

Task 4: Read from a File
Objective

Read content from a text file and display it on the screen.

Code

file = open("sample.txt", "r")
content = file.read()
file.close()

print("File Content:")
print(content)

Command to Run

python read_file.py

Explanation

The file is opened in read mode, data is read using the read() function, and the content is displayed on the terminal.

Sample Bash Commands Used

ls
cat sample.txt
python filename.py
