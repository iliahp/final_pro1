from tools.validator import Validator


class SelectCourse:
    def __init__(self, id, course, student, date_time, score):
        self.id = id
        self.course = course
        self.student = student
        self.date_time = date_time
        self.score = score

    def __str__(self):
        return f"{self.__dict__}"

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def course(self):
        return self.course

    @course.setter
    def course(self, course):
        self._course = course

    @property
    def student(self):
        return self.student

    @student.setter
    def student(self, student):
        self._student = student

    @property
    def score(self):
        return self.score

    @score.setter
    def score(self, score):
        self._score = Validator.score_validator(score, "invalid score ")

    @property
    def date_time(self):
        return self.date_time

    @date_time.setter
    def date_time(self, date_time):
        self._date_time = date_time
