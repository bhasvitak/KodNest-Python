class JobDescription:
    def __init__(
        self,
        job_id,
        company,
        role,
        location="Remote",
        is_active=True
    ):
        self.job_id = job_id
        self.company = company
        self.role = role
        self.location = location
        self.is_active = is_active

    def __str__(self):
        status = "Active" if self.is_active else "Closed"

        return (
            f"{self.job_id} | "
            f"{self.company} | "
            f"{self.role} | "
            f"{self.location} | "
            f"{status}"
        )


job_one = JobDescription(
    role="Python Developer",
    job_id=501,
    location="Bengaluru",
    company="TechNova"
)

job_two = JobDescription(
    company="CodeWorks",
    location="Hyderabad",
    role="Java Developer",
    job_id=502
)

job_three = JobDescription(
    is_active=False,
    role="Support Engineer",
    company="CloudNine",
    job_id=503
)

job_descriptions = [job_one, job_two, job_three]

for job in job_descriptions:
    print(job)