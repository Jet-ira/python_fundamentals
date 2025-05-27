#!/usr/bin/python
"""Write a function that takes a dictionary of student names and scores and returns 
the name of the student with the highest score."""

def top_student(scores):
    return max(scores, key=scores.get)

student_scores = {"Alice": 88, "Bob": 95, "Charlie": 90}
best = top_student(student_scores)
print(best)
