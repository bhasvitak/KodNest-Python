class StudentProfile:
    # Create the class-level object counter
    profile_count = 0

    def __init__(self, name):
        # Store the name
        self.name = name
        # Increase the shared counter
        StudentProfile.profile_count += 1

n = int(input())
students = []

# Read n names and create n StudentProfile objects
for i in range(n):
    student_name = input().strip()
    student_obj = StudentProfile(student_name)
    students.append(student_obj)

# Print the number of created profiles
print(f"Profiles Created: {StudentProfile.profile_count}")