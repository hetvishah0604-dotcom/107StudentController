from fastapi import Response
from models.student_model import Student


students = []


# CREATE STUDENT
async def create_student_controller(
    student: Student,
    response: Response
):
    try:
        for s in students:
            if s.id == student.id:
                response.status_code = 400
                return {
                    "isSuccess": False,
                    "message": "Student Id already exists"
                }

        students.append(student)

        response.status_code = 201

        return {
            "isSuccess": True,
            "message": "Student created successfully",
            "student": student
        }

    except Exception as e:
        print(e)
        response.status_code = 500

        return {
            "isSuccess": False,
            "message": "An error occurred while creating the student"
        }


# GET ALL STUDENTS
async def get_students_controller(
    response: Response
):
    try:

        response.status_code = 200

        return {
            "isSuccess": True,
            "message": "Students retrieved successfully",
            "students": students
        }

    except Exception as e:
        print(e)
        response.status_code = 500

        return {
            "isSuccess": False,
            "message": "An error occurred while retrieving students"
        }


# GET STUDENT BY ID
async def get_student_by_id_controller(
    student_id: int,
    response: Response
):
    try:

        for s in students:

            if s.id == student_id:

                response.status_code = 200

                return {
                    "isSuccess": True,
                    "message": "Student retrieved successfully",
                    "student": s
                }

        response.status_code = 404

        return {
            "isSuccess": False,
            "message": "Student not found"
        }

    except Exception as e:
        print(e)
        response.status_code = 500

        return {
            "isSuccess": False,
            "message": "An error occurred while retrieving the student"
        }


# UPDATE STUDENT
async def update_student_controller(
    student_id: int,
    student: Student,
    response: Response
):
    try:

        for s in students:

            if s.id == student_id:

                s.name = student.name
                s.email = student.email
                s.course = student.course
                s.semester = student.semester

                response.status_code = 200

                return {
                    "isSuccess": True,
                    "message": "Student updated successfully",
                    "student": s
                }

        response.status_code = 404

        return {
            "isSuccess": False,
            "message": "Student not found"
        }

    except Exception as e:
        print(e)
        response.status_code = 500

        return {
            "isSuccess": False,
            "message": "An error occurred while updating the student"
        }


# DELETE STUDENT
async def delete_student_controller(
    student_id: int,
    response: Response
):
    try:

        for s in students:

            if s.id == student_id:

                students.remove(s)

                response.status_code = 204

                return Response(status_code=204)

        response.status_code = 404

        return {
            "isSuccess": False,
            "message": "Student not found"
        }

    except Exception as e:
        print(e)
        response.status_code = 500

        return {
            "isSuccess": False,
            "message": "An error occurred while deleting the student"
        }