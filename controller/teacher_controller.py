from model.bl.teacher_bl import TeacherBl
from model.entity.teacher import Teacher
from tools.decorators import exception_handling


class TeacherController:

    @staticmethod
    @exception_handling
    def save(name, family, national_id, birthday, phone_number, salary, study, skill):
        teacher = Teacher(id, name, family, national_id, birthday, phone_number, salary, study, skill)
        TeacherBl.save(teacher)
        return True, f"teacher Saved : {teacher}"

    @staticmethod
    @exception_handling
    def edit(name, family, national_id, birthday, phone_number, salary, study, skill):
        teacher = Teacher(0, name, family, national_id, birthday, phone_number, salary, study, skill)
        TeacherBl.edit(teacher)
        return True, f"teacher  edited  : {teacher}"



    @staticmethod
    @exception_handling
    def remove(id):
        TeacherBl.remove(id)
        return True, f"teacher removed : {id}"


    @staticmethod
    @exception_handling
    def find_all():
        TeacherBl.find_all()


    @staticmethod
    @exception_handling
    def find_by_id(id):
        TeacherBl.find_by_id(id)