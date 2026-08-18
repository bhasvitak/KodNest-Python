class StudentProfile:
    def __init__(self, name, experience, skills):
        self.name = name
        self.experience = experience
        self.skills = skills

    def update_experience(self, new_experience):
        self.experience = new_experience

    def add_skill(self, new_skill):
        self.skills.append(new_skill)


# Reading initial input
name = input().strip()
experience = int(input())
skills = input().split()

# Creating the StudentProfile instance
student = StudentProfile(name, experience, skills)

# Reading update inputs
new_experience = int(input())
new_skill = input().strip()

# Updating the existing student profile object
student.update_experience(new_experience)
student.add_skill(new_skill)

# Printing the formatted output
print(f"Name: {student.name}")
print(f"Experience in Years: {student.experience}")
print(f"Skills: {', '.join(student.skills)}")