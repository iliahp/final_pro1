from template_maker import *


# da_maker("Course", ["id", "teacher", "title", "grade", "department"])
da_maker("Payment", ["id", "select_course", "amount", "description"])
da_maker("Person", ["id","name", "family", "national_id", "birthday", "phone_number"])
da_maker("student", ["id", "name", "family", "national_id", "birthday", "phone_number", "grade"])
da_maker("teacher", ["id", "name", "family", "national_id", "birthday", "phone_number", "salary", "study", "skill"])