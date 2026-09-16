def group_students(students):
    students_by_course = {}

    # Write your grouping logic here
    for i in students:
        if i[1] not in students_by_course:
            students_by_course[i[1]] = [i[0],]
        else:
            students_by_course[i[1]].append(i[0])

    return students_by_course

n = int(input())
students = []

for _ in range(n):
    name, course = input().split()
    students.append((name, course))

students_by_course = group_students(students)

for course, names in students_by_course.items():
    print(course + ": " + " ".join(names))