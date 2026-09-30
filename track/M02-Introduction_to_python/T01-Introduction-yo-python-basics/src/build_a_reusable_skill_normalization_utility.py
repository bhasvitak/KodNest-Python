class SkillUtility:
    @staticmethod
    def normalize_skill(skill):
        return skill.strip().lower()


skill = input()
result = SkillUtility.normalize_skill(skill)
print(f"Normalized Skill: {result}")