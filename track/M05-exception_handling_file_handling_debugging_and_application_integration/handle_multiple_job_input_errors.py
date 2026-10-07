requirements = ["Python", "SQL", "Git", "REST API"]

try:
    position = int(input())
    print(requirements[position])
except ValueError:
    print("Invalid position")
except IndexError:
    print("Requirement not found")