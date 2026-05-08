# Question 1
# Write a Python program to:

# Take a list of student marks
# Find the average
# Predict if a new student will pass (pass if > average)

marks = [40, 50, 60, 70]


def average(marks):
    total = sum(marks)
    averagee = total / len(marks)
    return averagee


new = int(input("Enter new student's marks: "))
if new > average(marks):
    print("Pass")
else:
    print("Fail")
