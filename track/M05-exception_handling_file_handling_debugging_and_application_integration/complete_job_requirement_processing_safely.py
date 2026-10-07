try:
    s = int(input())
    r = int(input())
    m = s/r*100
except ValueError:
    print("Invalid experience value")
except ZeroDivisionError:
    print("Required experience cannot be zero")
else:
    print(f"Experience Match: {m}")
finally:
    print("Job requirement processing complete")