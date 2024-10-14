from model.da.course_da import CourseDa


class CourseBl:

    @staticmethod
    def save(course):
        course_da = CourseDa()
        course_da.save(course)

    @staticmethod
    def edit(course):
        course_da = CourseDa()
        course_da.edit(course)

    @staticmethod
    def remove(id):
        course_da = CourseDa()
        course_da.remove(id)

    @staticmethod
    def find_by_id(id):
        course_da = CourseDa()
        return course_da.find_by_id(id)

    @staticmethod
    def find_all():
        course_da = CourseDa()
        return course_da.find_all()
