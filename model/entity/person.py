import re

from tools.validator import Validator


# id, name, family, birth_date, national_id, phone_number
class Person:
    def __init__(self, id, name, family, national_id, birthday, phone_number):
        self.id = id
        self.name = name
        self.family = family
        self.national_id = national_id
        self.birthday = birthday
        self.phone_number = phone_number

    def __str__(self):
        return f"{self.__dict__}"

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = Validator.name_validator(name, "invalid name ")

    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, family):
        self._family = Validator.name_validator(family, "invalid family ")

    @property
    def national_id(self):
        return self._national_id

    @national_id.setter
    def national_id(self, national_id):
        self._national_id = Validator.national_id_validator(national_id, "invalid National Id")

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, birthday):
        self._birthday = Validator.date_validator(birthday, "Invalid Birthday")

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        self._phone_number = Validator.phone_number_validator(phone_number, "invalid phone_number ")
