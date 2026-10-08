class CandidateProfile:
    def __init__(self, name, graduation_year, primary_skill):
        self.name = name
        self.graduation_year = graduation_year
        self.primary_skill = primary_skill

    # Create the factory method here
    @classmethod
    def from_record(cls, data):
        name, graduation_year, primary_skill = data.split(",")
        graduation_year = int(graduation_year)
        return cls(name, graduation_year, primary_skill)


record = input().strip()

candidate = CandidateProfile.from_record(record)

print(
    f"Candidate: {candidate.name} | "
    f"{candidate.graduation_year} | {candidate.primary_skill}"
)