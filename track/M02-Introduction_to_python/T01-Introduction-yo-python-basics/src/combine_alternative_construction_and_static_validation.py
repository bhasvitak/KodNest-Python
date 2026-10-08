class CandidateProfile:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    @staticmethod
    def is_valid_score(score):
        return 0 <= score <= 100

    @classmethod
    def from_string(cls, data):
        name, score_str = data.split(",")
        score = int(score_str)
        if cls.is_valid_score(score):
            return cls(name, score)
        return None


data = input().strip()
candidate = CandidateProfile.from_string(data)

if candidate is None:
    print("Invalid Candidate Data")
else:
    print(f"Candidate: {candidate.name}")
    print(f"Score: {candidate.score}")