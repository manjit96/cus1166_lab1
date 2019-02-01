from mymodules.models import Student
from mymodules.math_utils import average_grade

def __main__():

    roster = []

    roster.append(Student("Alex", 92))
    roster.append(Student("Sam", 95))
    roster.append(Student("Shane", 88))
    roster.append(Student("Elliot", 87))
    roster.append(Student("Sebastian", 97))
    roster.append(Student("Haley", 68))
    roster.append(Student("Caroline", 83))
    roster.append(Student("Abigail", 89))
    roster.append(Student("Leah", 76))
    roster.append(Student("Emily", 79))

    for student in roster:
        student.print_student_info()

    print(f"\nAverage of the student grades is: {average_grade(roster)}.")



__main__()
