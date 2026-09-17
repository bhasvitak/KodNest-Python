n = int(input())
temperatures = list(map(int, input().split()))

# Write your code here
sorted_temperatures = sorted(temperatures, reverse=True)

print(*sorted_temperatures)