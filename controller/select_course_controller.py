from model.bl.select_course_bl import SelectCourseBl
from model.da.select_course_da import SelectCourseDa
from model.entity.select_course import SelectCourse
from tools.decorators import exception_handling


class SelectCourseController:

    @staticmethod
    @exception_handling
    def save( course, student, date_time, score):
        select_course = SelectCourse(0, course, student, date_time, score)
        SelectCourseBl.save(select_course)
        return True, f"course Saved : {select_course}"

    @staticmethod
    @exception_handling
    def edit(id, course, student, date_time, score):
        select_course = SelectCourse(id, course, student, date_time, score)
        SelectCourseBl.edit(select_course)
        return True, f"course edited : {select_course}"

    @staticmethod
    @exception_handling
    def remove(id):
        SelectCourseBl.remove(id)
        return True, f"course removed : {id}"

    @staticmethod
    @exception_handling
    def find_all():
        SelectCourseBl.find_all()

        @staticmethod
        @exception_handling
        def find_by_id(id):
            SelectCourseBl.find_by_id(id)
