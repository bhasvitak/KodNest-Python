class LibraryBook:
    book_count = 0

    def __init__(self, title):
        self.title = title
        LibraryBook.book_count += 1

n = int(input())

for _ in range(n):
    title = input().strip()
    LibraryBook(title)

print(f"Books Created: {LibraryBook.book_count}")