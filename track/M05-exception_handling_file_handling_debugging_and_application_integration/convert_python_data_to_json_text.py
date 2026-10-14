import json

# Write your code here
name = input().strip()
score = int(input())
student = {
    "name": name,
    "score": score
}
print(json.dumps(student))