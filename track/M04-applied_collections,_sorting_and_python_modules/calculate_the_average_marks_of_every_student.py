n = int(input())
students = []

for _ in range(n):
    data = input().split()
    name = data[0]
    marks = list(map(int, data[1:]))

    students.append({
        "name": name,
        "marks": marks
    })

for student in students:
    total = 0

    for mark in student["marks"]:
        total += mark

    average = total / len(student["marks"])

    print(f"{student['name']}: {average:.2f}")