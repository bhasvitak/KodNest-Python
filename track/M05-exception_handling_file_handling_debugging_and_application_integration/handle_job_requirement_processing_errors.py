try:
    s = int(input())
    r = int(input())
    print(f"Experience Ratio: {s/r}")
except ValueError:
    print("Invalid experience")
except ZeroDivisionError:
    print("Required experience cannot be zero")