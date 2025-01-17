import mysql.connector

from person import Person

class PersonDa:

	def connect(self):
		self.connection = mysql.connector.connect(host="localhost", user="root", password="root123", database="mft")
		self.cursor = self.connection.cursor()

	def disconnect(self, commit=False):
		if commit:
			self.connection.commit()
		self.cursor.close()
		self.connection.close()

	def save(self, person):
		self.connect()
		self.cursor.execute("insert into person_tbl ( name, family, national_id, birthday, phone_number) values ("
							"%s,%s,%s,%s,%s)",[person.name, person.family, person.national_id, person.birthday, person.phone_number])
		self.disconnect(commit = True)

	def edit(self, person):
		self.connect()
		self.cursor.execute("update person_tbl set    where id=%s",[
			person.name, person.family, person.national_id, person.birthday, person.phone_number,person.id])
		self.disconnect(commit = True)

	def remove(self, id):
		self.connect()
		self.cursor.execute("delete from person_tbl where id=%s",[id])
		self.disconnect(commit = True)

	def find_all(self):
		self.connect()
		self.cursor.execute("select * from person_tbl ")
		person_list = [Person(*person) for person in self.cursor.fetchall()]
		self.disconnect()
		if person_list:
			return person_list

	def find_by_id(self, id):
		self.connect()
		self.cursor.execute("select * from person_tbl where id=%s", [id])
		person = self.cursor.fetchone()
		self.disconnect()
		if person:
			return Person(*person)

