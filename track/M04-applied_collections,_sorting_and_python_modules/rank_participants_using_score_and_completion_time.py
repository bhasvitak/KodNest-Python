n = int(input())
participants = []

for _ in range(n):
    name, score, completion_time = input().split()

    participants.append(
        (name, int(score), int(completion_time))
    )

# Write your code here
sorted_participants = sorted(participants, key=lambda participant: (-participant[1], participant[2]))

for i in sorted_participants:
    print(*i)