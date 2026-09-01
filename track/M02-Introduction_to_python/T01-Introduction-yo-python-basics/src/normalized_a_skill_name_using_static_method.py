class StudentProfile:
    @staticmethod
    def normalize_skill(skill_name):
        return "_".join(skill_name.strip().lower().split())


skill_name = input()

# Normalize the skill using the class name
b = StudentProfile.normalize_skill(skill_name)

# Print the normalized skill
print(f"Normalized Skill: {b}")