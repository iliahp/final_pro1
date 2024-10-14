from model.da.select_course_da import SelectCourseDa


class SelectCourseBl:

    @staticmethod
    def save(select_course):
        select_course_bl = SelectCourseDa()
        select_course_bl.save(select_course)

    @staticmethod
    def edit(select_course):
        select_course_bl = SelectCourseDa()
        select_course_bl.save(select_course)

    @staticmethod
    def remove(id):
        select_course_bl = SelectCourseDa()
        select_course_bl.save(id)

    @staticmethod
    def find_all():
        select_course_bl = SelectCourseDa()
        return select_course_bl.save()

    @staticmethod
    def find_by_id(id):
        select_course_bl = SelectCourseDa()
        return select_course_bl.save(id)
