import json

student = {
    "name": "Aarav",
    "score": 85,
    "skills": ["Python", "SQL"]
}

with open("student.json", "w") as file:
    json.dump(student, file)