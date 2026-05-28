from typing import Protocol
class paymentMethod(Protocol):
    def authorize_payment(self,amount:bool):
        print("Authorizing payment")
    
    def process_payment(self,amount:bool):
        print("Processing payment")
        
class creditcard:
    def authorize_payment(self,amount:bool):
        print("Authorizing creditcard payment")
        return True
    def process_payment(self,amount:bool):
        print("Processing payment ")
        return True

class paypal:
    def authorize_payment(self,amount:bool):
        print(f"Authorizing paypal payment of ${amount}")
        return True
    def process_payment(self,amount:bool):
        print(f"Processing payment in paypal of ${amount}")
        return True
    
    
def processorder(payment:paymentMethod, amount:int):
    if payment.authorize_payment(amount):
        payment.process_payment(amount)
        print("Payment successfull")
    else:
        print("Paymeny unsuccessfull")

creditpay = creditcard()
paypalpay = paypal()
processorder(creditpay,100.0)
processorder(paypalpay,200.0)