from model.da.student_da import StudentDa


class StudentBl:
    @staticmethod
    def save(student):
        student_da = StudentDa()
        student_da.save(student)

    @staticmethod
    def edit(student):
        student_da = StudentDa()
        student_da.edit(student)

    @staticmethod
    def remove(id):
        student_da = StudentDa()
        student_da.remove(id)

    @staticmethod
    def find_all():
        student_da = StudentDa()
        return student_da.find_all()

    @staticmethod
    def find_by_id(id):
        student_da = StudentDa()
        return student_da.find_by_id(id)
