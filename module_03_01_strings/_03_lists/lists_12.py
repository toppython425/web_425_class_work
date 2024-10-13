student_marks = [
    ["Bob", 11, 8, 9, 10],
    ["Jane", 12, 9, 12, 11],
    ["Mark", 10, 11, 8, 9]
]
print(student_marks[0])
print(student_marks[1])
print(student_marks[2])

print()

for student in student_marks:
    print(student)

print(student_marks[0][2])
print(student_marks[1][3])
print(student_marks[2][4])

student_marks = [
    {"Bob": [11, 8, 9, 10]},
    {"Jane": [12, 9, 12, 11]},
    {"Mark": [10, 11, 8, 9]}
]

print(student_marks[0]["Bob"])
print(student_marks[1]["Jane"])
print(student_marks[2]["Mark"])
