from model.da.payment_da import PaymentDa


class PaymentBl:

    @staticmethod
    def save(payment):
        payment_da = PaymentDa()
        payment_da.save(payment)

    @staticmethod
    def edit(payment):
        payment_da = PaymentDa()
        payment_da.edit(payment)

    @staticmethod
    def remove(id):
        payment_da = PaymentDa()
        payment_da.remove(id)

    @staticmethod
    def find_all():
        payment_da = PaymentDa()
        return payment_da.find_all()

    @staticmethod
    def find_by_id(id):
        payment_da = PaymentDa()
        return payment_da.find_by_id(id)
