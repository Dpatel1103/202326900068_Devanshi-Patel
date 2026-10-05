from fastapi import APIRouter, Response, status

from controllers.student_controller import (
    create_student,
    delete_student,
    get_student,
    get_students,
    update_student,
)
from models.student_model import Student

router = APIRouter()


@router.post("/students", response_model=Student, status_code=status.HTTP_201_CREATED)
def add_student(student: Student) -> Student:
    return create_student(student)


@router.get("/students", response_model=list[Student])
def list_students() -> list[Student]:
    return get_students()


@router.get("/students/{student_id}", response_model=Student)
def read_student(student_id: int) -> Student:
    return get_student(student_id)


@router.put("/students/{student_id}", response_model=Student)
def replace_student(student_id: int, student: Student) -> Student:
    return update_student(student_id, student)


@router.delete("/students/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_student(student_id: int) -> Response:
    delete_student(student_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
