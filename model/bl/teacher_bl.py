from model.da.teacher_da import teacherDa


class TeacherBl:
    @staticmethod
    def save(teacher):
        teacher_da = teacherDa()
        teacher_da.save(teacher)

    @staticmethod
    def edit(teacher):
        teacher_da = teacherDa()
        teacher_da.edit(teacher)

    @staticmethod
    def remove(id):
        teacher_da = teacherDa()
        teacher_da.remove(id)

    @staticmethod
    def find_all():
        teacher_da = teacherDa()
        teacher_da.find_all()

    @staticmethod
    def find_by_id(id):
        teacher_da = teacherDa()
        teacher_da.find_by_id(id)
