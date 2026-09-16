def calculate_discounted_prices(prices, discount_percentage):
    # Write your list comprehension here
    return [round(price-(discount_percentage*price)/100,2)for price in prices]

n = int(input())
prices = list(map(int, input().split()))
discount_percentage = int(input())

discounted_prices = calculate_discounted_prices(
    prices, discount_percentage
)

print(*discounted_prices)