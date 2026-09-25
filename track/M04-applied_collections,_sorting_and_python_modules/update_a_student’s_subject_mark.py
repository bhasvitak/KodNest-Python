name = input()
python_mark, sql_mark, java_mark = map(int, input().split())
subject = input()
new_mark = int(input())

student = {
    "name": name,
    "marks": {
        "Python": python_mark,
        "SQL": sql_mark,
        "Java": java_mark
    }
}

student["marks"][subject] = new_mark

print(student)