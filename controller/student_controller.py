from model.bl.student_bl import StudentBl
from model.entity.student import Student
from tools.decorators import exception_handling


class StudentController:
    @staticmethod
    @exception_handling
    def save(id,name, family, national_id, birthday, phone_number, grade):
        student = Student(0, name, family, national_id, birthday, phone_number, grade)
        StudentBl.save(student)
        return True, f"Student Saved : {student}"

    @staticmethod
    @exception_handling
    def edit(id,name, family, national_id, birthday, phone_number, grade):
        student = Student(id,name, family, national_id, birthday, phone_number,grade)
        StudentBl.edit(student)
        return True, f"Student Edited : {student}"

    @staticmethod
    @exception_handling
    def remove(id):
        StudentBl.remove(id)
        return True, f"Student Removed : {id}"

    @staticmethod
    @exception_handling
    def find_all():
        return True, StudentBl.find_all()

    @staticmethod
    @exception_handling
    def find_by_id(id):
        return True, StudentBl.find_by_id(id)
