class TrainingBatch:
    batch_name = "Python Batch 1"

    def __init__(self, student_name):
        self.student_name = student_name

    @classmethod
    def update_batch_name(cls, new_batch_name):
        cls.batch_name = new_batch_name


student1_name = input().strip()
student2_name = input().strip()
new_batch_name = input().strip()

# Create two TrainingBatch objects
s1 = TrainingBatch(student1_name)
s2 = TrainingBatch(student2_name)

# Update the shared batch name using the class method
TrainingBatch.update_batch_name(new_batch_name)

# Print the updated value through the class and both objects
print(f"Updated Batch: {TrainingBatch.batch_name}")
print(f"{s1.student_name}: {s1.batch_name}")
print(f"{s2.student_name}: {s2.batch_name}")