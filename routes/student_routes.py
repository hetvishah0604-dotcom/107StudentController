from fastapi import APIRouter, Response
from models.student_model import Student

from controllers.student_controller import (
    create_student_controller,
    get_students_controller,
    get_student_by_id_controller,
    update_student_controller,
    delete_student_controller
)


student_router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


@student_router.post("")
async def create_student(
    student: Student,
    response: Response
):
    return await create_student_controller(student, response)


@student_router.get("")
async def get_students(
    response: Response
):
    return await get_students_controller(response)


@student_router.get("/{student_id}")
async def get_student_by_id(
    student_id: int,
    response: Response
):
    return await get_student_by_id_controller(
        student_id,
        response
    )


@student_router.put("/{student_id}")
async def update_student(
    student_id: int,
    student: Student,
    response: Response
):
    return await update_student_controller(
        student_id,
        student,
        response
    )


@student_router.delete("/{student_id}")
async def delete_student(
    student_id: int,
    response: Response
):
    return await delete_student_controller(
        student_id,
        response
    )