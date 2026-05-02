""" TODO: Student Ranking System """

from typing import List, TypeAlias

# Type Alais
Student: TypeAlias = list[str | list[float]]

# Students data
students = [
    ["Alice", [15, 18, 12]],
    ["Bob", [10, 14, 16]],
    ["Charlie", [12, 11, 19]],
    ["Diana", [20, 15, 17]],
    ["Ethan", [8, 10, 12]],
    ["Fiona", [16, 14, 15]],
    ["George", [11, 9, 13]],
    ["Hannah", [18, 17, 19]],
    ["Ian", [14, 13, 14]],
    ["Julia", [19, 20, 18]],
    ["Kevin", [5, 7, 4]],     
    ["Laura", [9, 8, 10]],   
    ["Mike", [6, 12, 5]],     
    ["Nora", [15, 14, 16]],   
    ["Oscar", [4, 3, 5]]      
]

# Calculate averages

def average(student: Student) -> Student | float:
    name: str = student[0]
    grades: List[float] = student[1]
    avg: float = round(sum(student[1]) / len(student[1]), 2)
    
    return [name, grades, avg]

def student_averages(students: List[Student]) -> list[Student | float]:
    return [average(std) for std in students]

def sort_by_average(students: List[Student]) -> List[Student | float]:
    averages: List[Student | float] = student_averages(students)
    sort_by_avg_students: List[Student | float] = sorted(averages, key=lambda avg_student: avg_student[-1], reverse=True)
    
    return sort_by_avg_students

def find_top_three_students(students: List[Student]) -> List[Student | float]:
    sorted_students: List[Student | float] = sort_by_average(students)
    
    return sorted_students[:3]

def find_failed_students(students: List[Student]) -> List[Student | float]:
    averages: List[Student | float] = student_averages(students)
    failed_students: List[Student | float] = list(filter(lambda std: std[-1] < 10, averages))
    
    return failed_students

def calculate_class_average(students: List[Student]) -> float:
    averages: List[Student | float] = student_averages(students)

    total: float = 0
    for avg in averages:
        total += avg[-1]
    
    return round(total / len(averages), 2)


if __name__ == "__main__":
    print("\nStudent averages:",student_averages(students))
    print("\nStudent sort by averages:", sort_by_average(students))
    print("\nTop three students:", find_top_three_students(students))
    print("\nFailed students:", find_failed_students(students))
    print("\nClass average:", calculate_class_average(students))