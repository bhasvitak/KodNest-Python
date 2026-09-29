from collections import Counter

issues = input().split()

# Write your code here
issues_count = Counter(issues)

most_common = issues_count.most_common(2)

for i in most_common:
    print(f"{i[0]}: {i[1]}")