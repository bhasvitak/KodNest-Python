from student_result import display_details
import student_result

if __name__ == "__main__":
    name = input("Enter your name: ")
    rollno = input("Enter your roll no: ")
    marks1 = int(input("Enter your marks in subject 1: "))
    marks2 = int(input("Enter your marks in subject 2: "))
    marks3 = int(input("Enter your marks in subject 3: "))

    display_details(name,rollno,marks1,marks2,marks3)