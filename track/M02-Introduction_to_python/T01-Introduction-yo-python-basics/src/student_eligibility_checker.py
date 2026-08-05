# Read marks, attendance and project completion status
marks = int(input())
attendence = int(input())
pcs = input()
# Check the academic requirements
if marks >= 60 and attendence >= 75:
    # Check the project completion status
    if pcs == "yes":
        print("Eligible")
    else:
        print("Not Eligible")
else:
    print("Not Eligible")