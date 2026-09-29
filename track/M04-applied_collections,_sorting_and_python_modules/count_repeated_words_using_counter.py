from collections import Counter

words = input().split()

word_count = Counter(words)

for word, count in word_count.items():
    print(f"{word}: {count}")