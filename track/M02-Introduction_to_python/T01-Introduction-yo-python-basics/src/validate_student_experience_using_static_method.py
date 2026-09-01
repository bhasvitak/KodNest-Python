class StudentProfile:
    def __init__(self, name, experience):
        self.name = name
        self.experience = experience

    @staticmethod
    def is_valid_experience(experience):
        return 0 <= experience <= 40


name = input().strip()
experience = int(input())

# Validate the experience using the class name
a = StudentProfile.is_valid_experience(experience)

# Create and print the profile only when valid
if a:
    print("Profile Created")
    obj = StudentProfile(name, experience)
    print(f"Name: {obj.name}")
    print(f"Experience: {obj.experience} years")
else:
    print("Invalid Experience")