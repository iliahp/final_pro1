import mysql.connector

from model.entity.teacher import Teacher


class teacherDa:

    def connect(self):
        self.connection = mysql.connector.connect(host="localhost", user="root", password="root123", database="mft")
        self.cursor = self.connection.cursor()

    def disconnect(self, commit=False):
        if commit:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def save(self, teacher):
        self.connect()
        self.cursor.execute(
            "insert into teacher_tbl (name, family, national_id, birthday, phone_number, salary, study, skill) values (%s,%s,%s,%s,%s,%s,%s,%s)",
            [
                teacher.name, teacher.family, teacher.national_id, teacher.birthday, teacher.phone_number,
                teacher.salary, teacher.study, teacher.skill])
        self.disconnect(commit=True)

    def edit(self, teacher):
        self.connect()
        self.cursor.execute("update teacher_tbl set   where id=%s", [teacher.id, teacher.name, teacher.family, teacher.national_id, teacher.birthday, teacher.phone_number,
            teacher.salary, teacher.study, teacher.skill])
        self.disconnect(commit=True)

    def remove(self, id):
        self.connect()
        self.cursor.execute("delete from teacher_tbl where id=%s", [id])
        self.disconnect(commit=True)

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from teacher_tbl ")
        teacher_list = [teacher(*teacher) for teacher in self.cursor.fetchall()]
        self.disconnect()
        if teacher_list:
            return teacher_list

    def find_by_id(self, id):
        self.connect()
        self.cursor.execute("select * from teacher_tbl where id=%s", [id])
        teacher = self.cursor.fetchone()
        self.disconnect()
        if teacher:
            return teacher(*teacher)
