def create_squares(numbers):
    # Write your list comprehension here
    return [i*i for i in numbers]

n = int(input())
numbers = list(map(int, input().split()))

squares = create_squares(numbers)
print(*squares)