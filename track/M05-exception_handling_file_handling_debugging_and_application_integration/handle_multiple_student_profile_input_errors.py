skills = ["Python", "SQL", "Git", "HTML"]

try:
    skill_position = int(input())
    print(skills[skill_position])
except ValueError:
    print("Invalid position")
except IndexError:
    print("Skill not found")