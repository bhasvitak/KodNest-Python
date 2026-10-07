try:
    m = int(input())
    r = int(input())
    match_percentage = (m / r) * 100
except ValueError:
    print("Invalid skill count")
except ZeroDivisionError:
    print("Required skills cannot be zero")
else:
    print(f"Match Percentage: {match_percentage}")
finally:
    print("Match processing complete")