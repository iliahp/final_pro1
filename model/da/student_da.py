import mysql.connector
from model.entity.student import Student


class studentDa:

	def connect(self):
		self.connection = mysql.connector.connect(host="localhost", user="root", password="root123", database="mft")
		self.cursor = self.connection.cursor()

	def disconnect(self, commit=False):
		if commit:
			self.connection.commit()
		self.cursor.close()
		self.connection.close()

	def save(self, student):
		self.connect()
		#todo : complete sql command and parameters
		self.cursor.execute("insert into student_tbl (name, family, national_id, birthday, phone_number, grade) values (%s,%s,%s,%s,%s,%s)",
							[student.name, student.family, student.national_id, student.birthday, student.phone_number, student.grade])
		self.disconnect(commit = True)

	def edit(self, student):
		self.connect()
		#todo : complete sql command and parameters
		self.cursor.execute("update student_tbl set    where id=%s",
							[student.name, student.family, student.national_id, student.birthday, student.phone_number, student.grade,student.id])
		self.disconnect(commit = True)

	def remove(self, id):
		self.connect()
		self.cursor.execute("delete from student_tbl where id=%s",[id])
		self.disconnect(commit = True)

	def find_all(self):
		self.connect()
		self.cursor.execute("select * from student_tbl ")
		student_list = [student(*student) for student in self.cursor.fetchall()]
		self.disconnect()
		if student_list:
			return student_list

	def find_by_id(self, id):
		self.connect()
		self.cursor.execute("select * from student_tbl where id=%s", [id])
		student = self.cursor.fetchone()
		self.disconnect()
		if student:
			return student(*student)

