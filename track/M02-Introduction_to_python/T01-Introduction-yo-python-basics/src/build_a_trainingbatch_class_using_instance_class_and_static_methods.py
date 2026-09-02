class TrainingBatch:
    batch_name = "Python Batch 1"
    student_count = 0

    def __init__(self, student_name, attendance):
        self.student_name = student_name
        self.attendance = attendance
        TrainingBatch.student_count += 1

    def get_details(self):
        return f"{self.student_name}: {self.attendance}%"

    @classmethod
    def update_batch_name(cls, new_name):
        cls.batch_name = new_name

    @staticmethod
    def is_valid_attendance(attendance):
        return 0 <= attendance <= 100


# Read input
n = int(input())
students = []

for _ in range(n):
    name = input().strip()
    attendance = int(input())

    # Validate BEFORE creating the object
    if TrainingBatch.is_valid_attendance(attendance):
        student = TrainingBatch(name, attendance)
        students.append(student)

new_batch_name = input().strip()
TrainingBatch.update_batch_name(new_batch_name)

# Print results
print(f"Batch: {TrainingBatch.batch_name}")
print(f"Valid Students: {TrainingBatch.student_count}")
for student in students:
    print(student.get_details())