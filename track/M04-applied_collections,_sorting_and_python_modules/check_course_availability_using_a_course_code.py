def check_course_availability(courses, course_code):
    # Write your dictionary lookup logic here
    if course_code in courses.keys():
        if courses[course_code] != 0:
            return f"Seats available: {courses[course_code]}"
        else:
            return "Course full"
    else:
        return "Course not found"

courses = {
    "PY101": 25,
    "SQL201": 0,
    "DSA301": 12,
    "WEB401": 4
}

course_code = input()
print(check_course_availability(courses, course_code))