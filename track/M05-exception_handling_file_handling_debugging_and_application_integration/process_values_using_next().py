n = int(input())
quantities = list(map(int, input().split()))
k = int(input())

q_it = iter(quantities)
total_sum = 0

for i in range(k):
    try:
        total_sum += next(q_it)
    except StopIteration:
        break

print(total_sum)