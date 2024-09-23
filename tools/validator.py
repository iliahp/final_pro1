import re
from datetime import datetime, date


class Validator:
    @classmethod
    def name_validator(cls, name, message):
        if isinstance(name, str) and re.match(r"^[a-zA-Z\s]{2,30}$", name):
            return name
        else:
            raise ValueError(message)

    @classmethod
    def username_validator(cls, username, message):
        if re.match(r"^[\w@!#$%^&*\s]{2,30}$", username):
            return username
        else:
            raise ValueError(message)

    @classmethod
    def password_validator(cls, password, message):
        if re.match(r"^[\w@!#$%^&*\s]{2,16}$", password):
            return password
        else:
            raise ValueError(message)

    @classmethod
    def national_id_validator(cls, national_id, message):
        if isinstance(national_id, str) and re.match(r"^[0-9]{10}$", national_id):
            return national_id
        else:
            raise ValueError(message)

    @classmethod
    def phone_number_validator(cls, phone_number, message):
        if isinstance(phone_number, str) and re.match(r"^[0-9]{11}$", phone_number):
            return phone_number
        else:
            raise ValueError(message)

    @classmethod
    def salary_validator(cls, salary, message):
        if isinstance(salary, str) and 0 < int(salary) <= 10000:
            return salary
        else:
            raise ValueError(message)

    @classmethod
    def score_validator(cls, score, message):
        if isinstance(score, int) and 0 <= score <= 20:
            return score
        else:
            raise ValueError(message)

    @classmethod
    def grade_validator(cls, grade, message):
        if isinstance(grade, str) and 0 < int(grade) <= 12:
            return grade
        else:
            raise ValueError(message)

    @classmethod
    def date_validator(cls, _date, message):
        if isinstance(_date, date):
            return _date
        elif isinstance(_date, str):
            try:
                return datetime.strptime(_date, "%Y-%m-%d").date()
            except:
                raise ValueError(message)
        else:
            raise ValueError(message)
