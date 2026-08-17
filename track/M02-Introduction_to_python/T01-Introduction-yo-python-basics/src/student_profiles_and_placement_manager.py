class StudentProfile:
    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course

    def __str__(self):
        return f"{self.student_id} - {self.name} - {self.course}"


class PlacementManager:
    def __init__(self):
        self.student_profiles = []

    def add_student_profile(self, student_profile):
        # Add the received student object
        self.student_profiles.append(student_profile)

    def display_student_profiles(self):
        # Handle an empty collection
        # Display all student profiles
        if len(self.student_profiles) == 0:
            print("No Student Profiles available")
        else:
            for profile in self.student_profiles:
                print(profile)

    def filter_students_by_course(self, course):
        # Return all students whose course matches (case-insensitive)
        result = []
        for profile in self.student_profiles:
            if profile.course.lower() == course.lower():
                result.append(profile)
        return result


manager = PlacementManager()

n = int(input())

for _ in range(n):
    student_id = int(input())
    name = input().strip()
    course = input().strip()

    student = StudentProfile(student_id, name, course)
    manager.add_student_profile(student)

manager.display_student_profiles()

needed_course = input().strip()
result = manager.filter_students_by_course(needed_course)

if result:
    for profile in result:
        print(profile)
else:
    print(f"No students found for course - {needed_course}")