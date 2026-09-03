from abc import ABC, abstractmethod


class SkillAnalyzer(ABC):
    def __init__(self, student_skills, required_skills):
        self.student_skills = set(student_skills)
        self.required_skills = set(required_skills)

    def get_matched_skills(self):
        return self.student_skills & self.required_skills

    # Add abstract analyze()
    @abstractmethod
    def analyze(self):
        pass


class MatchScoreCalculator(SkillAnalyzer):
    def calculate_match_score(self):
        matched = len(self.get_matched_skills())
        required = len(self.required_skills)
        return matched / required * 100

    def analyze(self):
        score = self.calculate_match_score()
        return f"Match Score: {score:.2f}%"


class MissingSkillDetector(SkillAnalyzer):
    def get_missing_skills(self):
        return sorted(list(self.required_skills - self.student_skills))

    def analyze(self):
        missing = sorted(self.get_missing_skills())
        if missing:
            return f"Missing Skills: {', '.join(missing)}"
        return "Missing Skills: None"


student_skills = input().split()
required_skills = input().split()

m = MatchScoreCalculator(student_skills, required_skills)
d = MissingSkillDetector(student_skills, required_skills)

print(m.analyze())
print(d.analyze())