from typing import Protocol


class Payment(Protocol):

    def process_payment(self, amount):
        pass


class CreditCard:

    def process_payment(self, amount):
        print(f"Paid {amount} using Credit Card")


class UPI:

    def process_payment(self, amount):
        print(f"Paid {amount} using UPI")


def make_payment(method: Payment, amount):
    method.process_payment(amount)


c = CreditCard()
u = UPI()

make_payment(c, 500)
make_payment(u, 1000)