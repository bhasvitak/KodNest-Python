# Read the number of students
n = int(input())

# Initialize the total and counters
tm = 0
pc = 0
fc = 0

# Read and process each mark
for i in range(n):
    mark = int(input())
    tm = tm+mark
    
    if mark>=40:
        pc = pc+1
    else:
        fc=fc+1

# Display the summary
print(f"Total Marks: {tm}")
print(f"Passed Students: {pc}")
print(f"Failed Students: {fc}")

if fc == 0:
    print("Batch Result: All Passed")
else:
    print("Batch Result: Needs Improvement")