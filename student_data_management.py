
# Student Data Management Using Python Collections

# Dictionary containing student records
students = {
    101: ("Amit", "Computer", 85),
    102: ("Priya", "IT", 90),
    103: ("Rahul", "Mechanical", 78)
}

# 1. Add a new student
students[104] = ("Sneha", "Electrical", 88)
print("After adding a student:")
print(students)

# 2. Delete an existing student
del students[102]
print("\nAfter deleting a student:")
print(students)

# 3. Update student details
students[103] = ("Rahul", "Civil", 82)
print("\nAfter updating a student:")
print(students)

# 4. Display final student records
print("\nFinal Student Records:")
print("Roll No. | Name | Branch | Marks")

for roll_no, (name, branch, marks) in students.items():
    print(f"{roll_no} | {name} | {branch} | {marks}")

# Create a list of student names
student_names = [details[0] for details in students.values()]
print("\nStudent Names List:", student_names)

# Create a tuple for one student's details
student_tuple = students[101]
print("Student Tuple:", student_tuple)
