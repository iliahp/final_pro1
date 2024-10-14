from model.entity.course import Course
from model.bl.course_bl import CourseBl
from tools.decorators import exception_handling


class CourseController:

    @staticmethod
    @exception_handling
    def save(teacher, title, grade, department):
        course = Course(teacher, title, grade, department)
        CourseBl.save(course)
        return True, f"course saved : {course}"

    @staticmethod
    @exception_handling
    def edit(id, teacher, title, grade, department):
        course = Course(id, teacher, title, grade, department)
        CourseBl.edit(course)
        return True, f"course edited : {course}"

    @staticmethod
    @exception_handling
    def remove(id):
        CourseBl.remove(id)
        return True, f"course removed : {id}"

    @staticmethod
    @exception_handling
    def find_by_id(id):
        CourseBl.find_by_id(id)

    @staticmethod
    @exception_handling
    def find_all():
        CourseBl.find_all()
