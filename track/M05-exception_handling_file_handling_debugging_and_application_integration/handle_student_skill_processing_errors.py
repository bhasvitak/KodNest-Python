try:
    m = int(input())
    r = int(input())
    print(f"Match Percentage: {m/r*100}")
except ValueError:
    print("Invalid skill count")
except ZeroDivisionError:
    print("Required skills cannot be zero")