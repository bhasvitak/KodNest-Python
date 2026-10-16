def celsius_to_fahrenheit(celsius):
    # TODO: Implement logic to convert Celsius to Fahrenheit
    return celsius * 9/5 + 32

# TODO: Use map() to convert celsius_temperatures to Fahrenheit
celsius_temperatures = list(map(int, input().split()))  # Hardcoded list of temperatures for conversion
result = map(celsius_to_fahrenheit, celsius_temperatures)
print(list(result))