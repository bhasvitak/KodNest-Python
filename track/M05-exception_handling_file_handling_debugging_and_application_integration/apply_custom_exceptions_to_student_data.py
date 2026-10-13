class InvalidMarksError(Exception):
    pass

class InvalidAttendanceError(Exception):
    pass

marks = int(input())
attendance = int(input())

# Write your code here
try:
    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks must be between 0 and 100")
    elif attendance < 0 or attendance > 100:
        raise InvalidAttendanceError("Attendance must be between 0 and 100")
    print("Student data valid")
except Exception as e:
    print(e)