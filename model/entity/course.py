from tools.validator import Validator


class Course:
    def __init__(self, id, teacher, title, grade, department):
        self.id = id
        self.teacher = teacher
        self.title = title
        self.grade = grade
        self.department = department

    def __str__(self):
        return f"{self.__dict__}"

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def teacher(self):
        return self._teacher

    @teacher.setter
    def teacher(self, teacher):
        self._teacher = Validator.name_validator(teacher, "invalid name ")

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = Validator.name_validator(title, "invalid title ")

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, department):
        self._department = Validator.name_validator(department, "invalid department ")
