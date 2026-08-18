class StudentProfile:
    def __init__(self, student_id, name, course, experience, skills):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.experience = experience
        self.skills = skills

    def __str__(self):
        skills_text = ", ".join(self.skills)
        return (
            "STUDENT PROFILE\n"
            f"Student ID: {self.student_id}\n"
            f"Name: {self.name}\n"
            f"Course: {self.course}\n"
            f"Experience in Years: {self.experience}\n"
            f"Skills: {skills_text}"
        )

# Reading inputs
student_id = int(input())
name = input().strip()
course = input().strip()
experience = int(input())
skills = input().split()

# Create one StudentProfile object
student = StudentProfile(student_id, name, course, experience, skills)

# Print the profile using __str__()
print(student)