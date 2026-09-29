from collections import Counter

votes = input().split()

# Write your code here
vote_count = Counter(votes)

for i in vote_count:
    print(f"{i}: {vote_count[i]}")