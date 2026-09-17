n = int(input())
books = []

for _ in range(n):
    book_name, page_count = input().split()
    books.append((book_name, int(page_count)))

# Write your code here
sorted_books = sorted(books,key=lambda book:book[1])
for i in sorted_books:
    print(*i)