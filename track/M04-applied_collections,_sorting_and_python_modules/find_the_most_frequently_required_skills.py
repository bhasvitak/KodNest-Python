from collections import Counter

skills = input().split()

# Write your code here
skills_count = Counter(skills)

most_common_skill = skills_count.most_common(1)

for i in most_common_skill:
    print(f"{i[0]}: {i[1]}")