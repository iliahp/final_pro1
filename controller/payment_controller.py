from model.bl.payment_bl import PaymentBl
from model.entity.payment import Payment
from tools.decorators import exception_handling


class PaymentController:

    @staticmethod
    @exception_handling
    def save(select_course, amount, description):
        payment = Payment(select_course, amount, description)
        PaymentBl.save(payment)
        return True, f"transaction saved : {payment}"

    @staticmethod
    @exception_handling
    def edit(id, select_course, amount, description):
        payment = Payment(id, select_course, amount, description)
        PaymentBl.edit(payment)
        return True, f"transaction edited : {payment}"

    @staticmethod
    @exception_handling
    def remove(id):
        payment = Payment(id)
        PaymentBl.remove(payment)
        return True, f"transaction removed : {id}"

    @staticmethod
    @exception_handling
    def find_by_id(id):
        return True, PaymentBl.find_by_id(id)

    @staticmethod
    @exception_handling
    def find_all():
        return True, PaymentBl.find_all()
