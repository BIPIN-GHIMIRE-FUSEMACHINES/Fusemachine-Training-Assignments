'''
[Interface Segregation Principle (ISP)] Download the python file from this link.
Suppose we have an interface called PaymentProcessor that defines methods for
processing payments and refunds. Then we have a class called
OnlinePaymentProcessor that implements the PaymentProcessor interface. However,
some parts of our system only need to process payments and do not handle refunds.
Redesign this program to follow the Interface Segregation Principle (ISP) principle
which represents that “Clients should not be forced to depend upon methods that
they do not use. Interfaces belong to clients, not to hierarchies.” (Hint: Create two
different classes in which one class use interfaces for process payment and another
class can process and refund payment both)
'''
from abc import abstractmethod

class PaymentProcessor:
    @abstractmethod
    def process_payment(self, amount):
        pass


class RefundProcessor:
    @abstractmethod
    def process_refund(self, amount):
        pass


class OnlinePaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing payment of ${amount}")


class OnlinePaymentRefundProcessor(PaymentProcessor, RefundProcessor):
    def process_payment(self, amount):
        print(f"Processing payment of ${amount}")

    def process_refund(self, amount):
        print(f"Processing refund of ${amount}")


def perform_payment(payment_processor, amount):
    payment_processor.process_payment(amount)


def perform_refund(refund_processor, amount):
    refund_processor.process_refund(amount)


if __name__ == "_main_":
    online_payment_processor = OnlinePaymentProcessor()
    online_payment_refund_processor = OnlinePaymentRefundProcessor()

    perform_payment(online_payment_processor, 100)
    perform_refund(online_payment_refund_processor, 50)