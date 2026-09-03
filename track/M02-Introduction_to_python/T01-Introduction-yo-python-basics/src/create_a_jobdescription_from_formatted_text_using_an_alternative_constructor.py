class JobDescription:
    def __init__(self, role, company, minimum_experience, required_skills):
        self.role = role
        self.company = company
        self.minimum_experience = minimum_experience
        self.required_skills = required_skills

    @classmethod
    def from_text(cls, data):
        role, company, minimum_experience, required_skills = data.split(";")
        
        # Strip each skill using a list comprehension inside brackets []
        skills_list = [skill.strip() for skill in required_skills.split(",")]
        
        return cls(
            role.strip().title(),
            company.strip(),
            int(minimum_experience),
            skills_list
        )


data = input()
job = JobDescription.from_text(data)

print(f"Role: {job.role}")
print(f"Company: {job.company}")
print(f"Minimum Experience: {job.minimum_experience} years")
print(f"Required Skills: {', '.join(job.required_skills)}")