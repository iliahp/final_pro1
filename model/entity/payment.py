
class Payment:
    def __init__(self, id, select_course, amount, description):
        self.id = id
        self.select_course = select_course
        self.amount = amount
        self.description = description

    def __str__(self):
        return f"{self.__dict__}"

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def select_course(self):
        return self._select_course

    @select_course.setter
    def select_course(self, _select_course):
        self._select_course = _select_course

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount

    @property
    def desciription(self):
        return self._description

    @desciription.setter
    def desciription(self, description):
        self._description = description
