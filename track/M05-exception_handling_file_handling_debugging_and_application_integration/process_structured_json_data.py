import json

# Write your code here
student = input()
data = json.loads(student)
print(data["name"])
print(sum(data["scores"]))