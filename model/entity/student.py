from model.entity.person import Person
from tools.validator import Validator


class Student(Person):
    def __init__(self, id, name, family, national_id, birthday, phone_number, grade):
        super().__init__(id, name, family, national_id, birthday, phone_number)
        self.grade = grade

    def __str__(self):
        return f"{self.__dict__}"

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = Validator.grade_validator(grade, "invalid grade ")
