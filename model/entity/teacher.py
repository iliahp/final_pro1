from model.entity.person import Person
from tools.validator import Validator


class Teacher(Person):
    def __init__(self, id, name, family, national_id, birthday, phone_number, salary, study, skill):
        super().__init__(id, name, family, national_id, birthday, phone_number)
        self.salary = salary
        self.study = study
        self.skill = skill

    def __str__(self):
        return f"{self.__dict__}"

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        self._salary = Validator.salary_validator(salary, "invalid salary ")

    @property
    def study(self):
        return self._study

    @study.setter
    def study(self, study):
        self._study = study

    @property
    def skill(self):
        return self._skill

    @skill.setter
    def skill(self, skill):
        self._skill = skill
