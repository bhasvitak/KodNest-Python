def convert_to_fahrenheit(celsius_temperatures):
    # Write your list comprehension here
    return [i*9/5+32 for i in celsius_temperatures]

n = int(input())
celsius_temperatures = list(map(int, input().split()))

fahrenheit_temperatures = convert_to_fahrenheit(
    celsius_temperatures
)

print(*fahrenheit_temperatures)