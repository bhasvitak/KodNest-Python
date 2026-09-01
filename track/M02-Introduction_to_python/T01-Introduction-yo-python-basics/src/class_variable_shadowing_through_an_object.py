class TrainingBatch:
    # Create the shared batch-name variable
    batch_name = "Python Batch 1"

    def __init__(self, student_name):
        # Store the student name
        self.student_name = student_name


student1_name = input().strip()
student2_name = input().strip()
special_batch = input().strip()
new_shared_batch = input().strip()

# Create two TrainingBatch objects
obj1 = TrainingBatch(student1_name)
obj2 = TrainingBatch(student2_name)

# Create an object-specific batch value for student1
obj1.batch_name = special_batch

# Update the shared class variable
TrainingBatch.batch_name = new_shared_batch

# Output the results
print(f"Class Batch: {TrainingBatch.batch_name}")
print(f"{obj1.student_name} Batch: {obj1.batch_name}")
print(f"{obj2.student_name} Batch: {obj2.batch_name}")