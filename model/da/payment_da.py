import mysql.connector

from model.entity.payment import Payment


class PaymentDa:

    def connect(self):
        self.connection = mysql.connector.connect(host="localhost", user="root", password="root123", database="mft")
        self.cursor = self.connection.cursor()

    def disconnect(self, commit=False):
        if commit:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def save(self, payment):
        self.connect()
        # todo : complete sql command and parameters
        self.cursor.execute("insert into payment_tbl (select_course_id, amount, description) values (%s,%s,%s)",
                            [Payment.select_course, Payment.amount, Payment.description])
        self.disconnect(commit=True)

    def edit(self, payment):
        self.connect()
        # todo : complete sql command and parameters
        self.cursor.execute("update payment_tbl set    where id=%s",
                            [Payment.select_course_id, Payment.amount, Payment.description, Payment.id])
        self.disconnect(commit=True)

    def remove(self, id):
        self.connect()
        self.cursor.execute("delete from payment_tbl where id=%s", [id])
        self.disconnect(commit=True)

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from payment_tbl ")
        payment_list = [Payment(*payment) for payment in self.cursor.fetchall()]
        self.disconnect()
        if payment_list:
            return payment_list

    def find_by_id(self, id):
        self.connect()
        self.cursor.execute("select * from payment_tbl where id=%s", [id])
        payment = self.cursor.fetchone()
        self.disconnect()
        if payment:
            return Payment(*payment)
