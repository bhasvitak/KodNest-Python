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
        if not self.required_skills:
            return "Match Score: 0.00%"

        matched_count = sum(
            1 for skill in self.required_skills if skill in self.student_skills
        )
        score = (matched_count / len(self.required_skills)) * 100
        return f"Match Score: {score:.2f}%"


class MissingSkillDetector(SkillAnalyzer):

    def analyze(self):
        missing = [
            skill
            for skill in self.required_skills
            if skill not in self.student_skills
        ]
        if missing:
            return f"Missing Skills: {' '.join(missing)}"
        return "Missing Skills: None"


def run_analyzers(analyzers):
    for analyzer in analyzers:
        print(analyzer.analyze())


if __name__ == "__main__":
    student_skills = input().split()
    required_skills = input().split()

    obj1 = MatchScoreCalculator(student_skills, required_skills)
    obj2 = MissingSkillDetector(student_skills, required_skills)

    analyzers = [obj1, obj2]

    run_analyzers(analyzers)