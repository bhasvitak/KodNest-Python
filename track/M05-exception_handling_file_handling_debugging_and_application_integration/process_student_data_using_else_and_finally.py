try:
    n = int(input())
except ValueError:
    print("Invalid experience")
else:
    print(f"Experience: {n}")
finally:
    print("Student processing complete")