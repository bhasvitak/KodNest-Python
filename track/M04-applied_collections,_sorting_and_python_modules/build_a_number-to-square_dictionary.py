def build_square_dictionary(numbers):
    # Write your dictionary comprehension here
    return {number: number * number for number in numbers}


n = int(input())
numbers = list(map(int, input().split()))

square_by_number = build_square_dictionary(numbers)

for number, square in square_by_number.items():
    print(number, square)