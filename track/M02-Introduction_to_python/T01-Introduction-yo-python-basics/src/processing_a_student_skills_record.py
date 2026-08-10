# Read and store five skills
skills = []
for i in range(5):
    skills.append(input())

# Convert the list into a tuple
skill_record = tuple(skills)

# Create the required slices
a = skill_record[:3]
b = skill_record[-2:]
c = skill_record[::2]
d = skill_record[::-1]

# Display all required results
print(f"Skill Record: {skill_record}")
print(f"First Three: {a}")
print(f"Last Two: {b}")
print(f"Alternate Skills: {c}")
print(f"Reversed Skills: {d}")