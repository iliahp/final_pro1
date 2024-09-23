from model.da.person_da import PersonDa
from model.entity.person import Person



class PersonBl:
    @staticmethod
    def save(person):
        person_da = PersonDa()
        return person_da.save(person)