n = int(input())
transactions = list(map(int, input().split()))

# Write your code here
sorted_transactions = sorted(transactions)

print(*sorted_transactions)
print(*transactions)