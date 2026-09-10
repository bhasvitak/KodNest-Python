from abc import ABC, abstractmethod


class SkillAnalyzer(ABC):
    def __init__(self, student_skills, required_skills):
        self.student_skills = student_skills
        self.required_skills = required_skills

    @abstractmethod
    def analyze(self):
        pass


class MatchScoreCalculator(SkillAnalyzer):
    def analyze(self):
        matched = set(self.student_skills) & set(self.required_skills)
        score = (len(matched) / len(self.required_skills)) * 100
        return f"Match Score: {score:.2f}%"


class MissingSkillDetector(SkillAnalyzer):
    def analyze(self):
        missing = [
            skill
            for skill in self.required_skills
            if skill not in self.student_skills
        ]
        if missing:
            return f"Missing Skills: {', '.join(missing)}"
        return "Missing Skills: None"


class RequiredSkillCountAnalyzer:
    # Add constructor and analyze()
    def __init__(self, required_skills):
        self.required_skills = required_skills

    def analyze(self):
        return f"Required Skill Count: {len(self.required_skills)}"


def run_analyzers(analyzers):
    # Call analyze() for every object
    for i in analyzers:
        print(i.analyze())


student_skills = input().split()
required_skills = input().split()

m = MatchScoreCalculator(student_skills, required_skills)
d = MissingSkillDetector(student_skills, required_skills)
r = RequiredSkillCountAnalyzer(required_skills)

analyzers = [m, d, r]
run_analyzers(analyzers)