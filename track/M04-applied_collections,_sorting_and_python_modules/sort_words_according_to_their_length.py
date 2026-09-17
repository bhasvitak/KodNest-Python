n = int(input())
words = input().split()

# Write your code here
sorted_words = sorted(words,key=lambda word : len(word))
print(*sorted_words)