class StudentProfile:
    def __init__(
        self,
        student_id,
        name,
        course,
        score,
        skills,
        is_placed
    ):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.score = score
        self.skills = skills
        self.is_placed = is_placed

    def has_skill(self, skill_name):
        # Search for skill_name and return True or False
        for i in self.skills:
            if i.lower() == skill_name.lower():
                return True
        return False


student_id = int(input())
name = input().strip()
course = input().strip()
score = float(input())
skills_input = input().strip()
placement_input = input().strip()
skill_to_find = input().strip()

skills = [
    skill.strip()
    for skill in skills_input.split(",")
    if skill.strip()
]

is_placed = placement_input.lower() == "yes"

# Create one StudentProfile object
student = StudentProfile(student_id, name, course, score, skills, is_placed)

# Call has_skill() and print the required result
if student.has_skill(skill_to_find):
    print("Skill Found")
else:
    print("Skill  Not Found")