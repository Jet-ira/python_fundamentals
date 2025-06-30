#!/usr/bin/python
"""Create a tuple that contains a student’s info: (name, age, department, GPA)
Print each element of the tuple. Try changing the name (and observe what happens).
Explain why tuples are immutable in a comment"""


student_info = ("John Doe", 20, "Computer Science", 3.85)


print("Student Information:")
print("Name:", student_info[1])
print("Age:", student_info[2])
print("Department:", student_info[2])
print("GPA:", student_info[3])


# This will raise a TypeError because tuples are immutable
try:
    student_info[0] = "Jane Smith"
except TypeError as e:
    print("\nError:", e)


# Tuples are immutable, meaning their values cannot be changed after creation.
# This makes them useful for storing constant data or records that shouldn't be modified.
