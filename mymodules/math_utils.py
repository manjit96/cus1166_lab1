from mymodules import models

def average_grade(roster):
    average = 0
    for student in roster:
        average += student.get_grade()
    return average/len(roster)
