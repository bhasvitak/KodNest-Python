class StudentProfile:
    # Create the is_valid_skill() static method
    @staticmethod
    def is_valid_skill(skill_name):
        if not skill_name.strip():
            return False
        for char in skill_name:
            if not (('a' <= char <= 'z') or ('A' <= char <= 'Z') or (char == " ")):
                return False
        return True

    # Create the normalize_skill() static method
    @staticmethod
    def normalize_skill(skill_name):
        words = skill_name.strip().lower().split()
        return "_".join(words)


skill_name = input()

# Validate the skill using the class name
if StudentProfile.is_valid_skill(skill_name):
    print("Valid Skill")
    print(f"Normalized Skill: {StudentProfile.normalize_skill(skill_name)}")
else:
    print("Invalid Skill")