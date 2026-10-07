try:
    s = int(input())
    print(f"Required Experience: {s}")
except ValueError:
    print("Invalid experience requirement")