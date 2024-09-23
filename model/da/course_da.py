import mysql.connector

from model.entity.course import Course


class CourseDa:

    def connect(self):
        self.connection = mysql.connector.connect(host="localhost", user="root", password="root123", database="mft")
        self.cursor = self.connection.cursor()

    def disconnect(self, commit=False):
        if commit:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def save(self, course):
        self.connect()
        self.cursor.execute("insert into course_tbl ( teacher_id, title, grade, department) values (%s,%s,%s,%s)",
                            [course.teacher.id, course.title, course.grade, course.department])
        self.disconnect(commit=True)

    def edit(self, course):
        self.connect()
        self.cursor.execute("update course_tbl set    where id=%s",
                            [course.teacher.id, course.title, course.grade, course.department, course.id])
        self.disconnect(commit=True)

    def remove(self, id):
        self.connect()
        self.cursor.execute("delete from course_tbl where id=%s", [id])
        self.disconnect(commit=True)

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from course_tbl ")
        course_list = [Course(*course) for course in self.cursor.fetchall()]
        self.disconnect()
        if course_list:
            return course_list

    def find_by_id(self, id):
        self.connect()
        self.cursor.execute("select * from course_tbl where id=%s", [id])
        course = self.cursor.fetchone()
        self.disconnect()
        if course:
            return Course(*course)
