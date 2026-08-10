student_count = int(input())
marks = []

for index in range(student_count):
    marks.append(int(input()))

position = int(input())
corrected_mark = int(input())
passing_mark = int(input())

list_index = position - 1
marks[list_index] = corrected_mark

total_marks = sum(marks)
average_marks = total_marks / student_count
highest_mark = max(marks)
lowest_mark = min(marks)

passed_students = 0

for mark in marks:
    if mark >= passing_mark:
        passed_students += 1

print(f"Updated Marks: {marks}")
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks}")
print(f"Highest Mark: {highest_mark}")
print(f"Lowest Mark: {lowest_mark}")
print(f"Passed Students: {passed_students}")