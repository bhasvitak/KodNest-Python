def student_details(name, rollno):
    return f"Name: {name}\n"f"Roll No: {rollno}\n"

def calculate_total(m1,m2,m3):
    total = m1+m2+m3
    return total

def calculate_average(total):
    average = total/3
    return average

def get_result(average):
    if average >= 40:
        return "Pass"
    else:
        return "Fail"
    
def show_grade(average):
    if average >=90:
        return "A"
    elif average >=75:
        return "B"
    elif average >=59:
        return "C"
    elif average >=40:
        return "D"
    else:
        return "F"

def display_details(name,rollno,marks1,marks2,marks3):
    print(f"Student Name: {name}")
    print(f"Roll No: {rollno}")
    total = calculate_total( marks1,marks2,marks3)
    print(f"Total Marks: {total}")
    average = calculate_average(total)
    print(f"Average Mark : {average}")
    result = get_result(average)
    print(f"Result: {result}")
    grade = show_grade(average)
    print(f"Grade : {grade}")

if __name__ == "__main__":
    name = input("Enter your name: ")
    rollno = input("Enter your roll no: ")
    marks1 = int(input("Enter your marks in subject 1: "))
    marks2 = int(input("Enter your marks in subject 2: "))
    marks3 = int(input("Enter your marks in subject 3: "))

    display_details(name,rollno,marks1,marks2,marks3)