class SkillAnalyzer:
    def __init__(self, student_skills, required_skills):
        self.student_skills = student_skills
        self.required_skills = required_skills


class MissingSkillDetector(SkillAnalyzer):
    def get_missing_skills(self):
        return sorted(self.required_skills - self.student_skills)


student_skills = input().split()
required_skills = input().split()

# Create the detector and display missing skills
detector = MissingSkillDetector(student_skills, required_skills)
missing = detector.get_missing_skills()

if missing:
    print(f"Missing Skills: {', '.join(missing)}")
else:
    print("Missing Skills: None")