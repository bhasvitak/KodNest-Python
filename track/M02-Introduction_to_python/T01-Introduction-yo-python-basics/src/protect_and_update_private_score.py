class StudentProfile:

    def __init__(self, name, initial_score):
        self.name = name
        self.__score = initial_score

    def get_score(self):
        return self.__score

    def set_score(self, new_score):
        if 0 <= new_score <= 100:
            self.__score = new_score
            return True
        return False


# Read inputs
name = input().strip()
initial_score = int(input())
new_score = int(input())

# Create one StudentProfile object
student = StudentProfile(name, initial_score)

# Call set_score() and store its Boolean result
value = student.set_score(new_score)

# Display the update result
if value:
    print("Score Updated")
else:
    print("Invalid Score")

# Display the name and final score
print(f"Name: {student.name}")
print(f"Final Score: {student.get_score()}")