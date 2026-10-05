from fastapi import HTTPException

from models.student_model import Student

students: dict[int, Student] = {}


def create_student(student: Student) -> Student:
    if student.id in students:
        raise HTTPException(status_code=409, detail="Student with this ID already exists")
    students[student.id] = student
    return student


def get_students() -> list[Student]:
    return list(students.values())


def get_student(student_id: int) -> Student:
    student = students.get(student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


def update_student(student_id: int, updated_student: Student) -> Student:
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    student = updated_student.model_copy(update={"id": student_id})
    students[student_id] = student
    return student


def delete_student(student_id: int) -> None:
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    del students[student_id]
