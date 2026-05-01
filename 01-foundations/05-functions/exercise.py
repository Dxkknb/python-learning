"""
-------------------------------------
|     STUDENT MANAGEMENT SYSTEM     |
-------------------------------------
"""
from typing import TypedDict
from enum import Enum
import re
import secrets

# Types
class Student(TypedDict, total=False):
    id: str
    name: str
    age: int
    grades: list[float]
    average: float

class Options(Enum):
    ADD_STUDENT = 1
    VIEW_STUDENT = 2
    SEARCH_STUDENT = 3
    ADD_GRADES = 4
    CALCULATE_AVERAGE_GRADE = 5
    SHOW_BEST_STUDENT = 6
    SHOW_FAILED_STUDENTS = 7
    DELETE_STUDENT = 8
    EXIT = 9

MENU = """
===== STUDENT MANAGEMENT SYSTEM =====

1. Add student
2. View students
3. Search student
4. Add grades
5. Calculate averages
6. Show best student
7. Show failed students
8. Delete student
9. Exit
"""

MIN_AGE: int = 12
MAX_AGE: int = 50
MIN_TOTAL_GRADES: int = 2
PASSING_GRADE: float = 10.0

# Utils

def generate_id() -> str:                             
    return secrets.token_hex(3)

def average(grades: list[float]) -> float:
    if not grades:                                    
        print("No grades provided!")
        return 0.0
    return round(sum(grades) / len(grades), 2)

def find_student_by_id(student_id: str) -> tuple[int, Student] | None:
    for i, student in enumerate(students):
        if student["id"] == student_id:
            return i, student
    return None

students: list[Student] = [
    {"id": generate_id(), "name": "Alice", "age": 20, "grades": [15, 18, 12]},
    {"id": generate_id(), "name": "Kouassi Germain", "age": 30, "grades": [16, 17, 10]},
    {"id": generate_id(), "name": "John Doe", "age": 17, "grades": [15, 18, 11]},
    {"id": generate_id(), "name": "Kouassi Jacques", "age": 27, "grades": [17, 12, 10]},
]

# Validation

def check_valid_name(name: str) -> bool:
    pattern = r"^[a-zA-Z]{3,25}(\s[a-zA-Z]{3,25})?$"
    return bool(re.fullmatch(pattern, name))

def get_valid_name() -> str:
    while True:
        name = input("Provide your name: ").strip()
        if check_valid_name(name):
            return name
        print("Provide a valid name")

def get_valid_grade(prompt: str) -> float | None:    
    try:
        grade = float(input(prompt))
        if 0 <= grade <= 20:
            return grade
        print("Grade must be between 0 and 20.")
        return None
    except ValueError:
        print("Invalid grade, must be a number.")
        return None

# Core functionalities

def get_student_data() -> Student | None:
    try:
        name = input("Student name: ").strip()
        if not check_valid_name(name):                 
            print("Invalid student name!")
            return None

        age = int(input("Student age: "))
        if not (MIN_AGE <= age <= MAX_AGE):           
            print(f"Student age must be between {MIN_AGE} and {MAX_AGE}.")
            return None

        grades: list[float] = []
        i = 1
        while i <= MIN_TOTAL_GRADES:
            grade = get_valid_grade(f"Grade {i}: ")
            if grade is not None:
                grades.append(grade)
                i += 1

        return {"id": generate_id(), "name": name, "age": age, "grades": grades}

    except ValueError:
        print("Invalid input: age must be a number.")
        return None

def add_student(student: Student | None) -> None:
    if not student:
        print("Invalid student data.")
        return
    students.append(student)
    print("Student added successfully.")

def show_student(student: Student) -> str:
    grades_str = ", ".join(str(g) for g in student["grades"])
    return (
        f"\nID: {student['id']}"
        f"\nName: {student['name']}"
        f"\nAge: {student['age']}"
        f"\nGrades: {grades_str}"
        f"\nAverage: {average(student['grades'])}/20\n"
    )

def view_students(student_list: list[Student]) -> None:
    if not student_list:                          
        print("No students to display.")
        return
    for student in student_list:
        print(show_student(student))
        print("-----------------------------")

def search_student(name: str) -> None:
    found = [s for s in students if name.lower() in s["name"].lower()]
    if found:
        view_students(found)
    else:
        print("No student found.")

def add_grade() -> None:
    student_id = input("Provide the id of the student: ").strip()
    result = find_student_by_id(student_id)           

    if not result:
        print("Student not found.")
        return

    idx, student = result
    grade = get_valid_grade("Add grade: ")

    if grade is not None:
        students[idx]["grades"].append(grade)
        print("Grade added successfully.")
        print(show_student(students[idx]))

def calculate_averages() -> None:                      
    for student in students:
        student["average"] = average(student["grades"])

def show_best_student() -> None:
    if not students:
        print("No students available.")
        return
    calculate_averages()
    best = max(students, key=lambda s: s.get("average", 0))
    print(show_student(best))

def show_failed_students() -> None:
    calculate_averages()
    failed = [s for s in students if s.get("average", 0) < PASSING_GRADE]
    if failed:
        view_students(failed)
    else:
        print("No students failed!")

def delete_student() -> None:                          
    student_id = input("Provide the id of the student: ").strip()
    result = find_student_by_id(student_id)

    if not result:
        print("Student not registered.")
        return

    _, student = result
    students.remove(student)                           
    print("Student deleted successfully!")
    print(show_student(student))

def main() -> None:                                    
    print(MENU)
    actions = {                                       
        Options.ADD_STUDENT.value:            lambda: add_student(get_student_data()),
        Options.VIEW_STUDENT.value:           lambda: view_students(students),
        Options.SEARCH_STUDENT.value:         lambda: search_student(get_valid_name()),
        Options.ADD_GRADES.value:             add_grade,
        Options.CALCULATE_AVERAGE_GRADE.value: calculate_averages,
        Options.SHOW_BEST_STUDENT.value:      show_best_student,
        Options.SHOW_FAILED_STUDENTS.value:   show_failed_students,
        Options.DELETE_STUDENT.value:         delete_student,
    }

    while True:
        try:
            choice = int(input("Choose an option: "))

            if choice == Options.EXIT.value:
                print("Quit Student Management System")
                break

            action = actions.get(choice)
            if action:
                action()
            else:
                print("Invalid option, choose between 1 and 9.")

        except ValueError:
            print("Type a valid option number.")

if __name__ == "__main__":
    main()