n = int(input())
prices = list(map(int, input().split()))
k = int(input())

# Write your code here
p_it = iter(prices)
sum = 0
if k>n:
    for i in range(n):
        sum = sum+next(p_it)
else:
    for i in range(k):
        sum = sum+next(p_it)
print(sum)