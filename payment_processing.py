from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class PayPal(PaymentGateway):
    def process_payment(self, amount):
        print(f"Processing ${amount} payment via PayPal")

class Stripe(PaymentGateway):
    def process_payment(self, amount):
        print(f"Processing ${amount} payment via Stripe")

class PaymentGatewayFactory(ABC):
    @abstractmethod
    def create_payment_gateway(self):
        pass

class PayPalFactory(PaymentGatewayFactory):
    def create_payment_gateway(self):
        return PayPal()

class StripeFactory(PaymentGatewayFactory):
    def create_payment_gateway(self):
        return Stripe()
def main():
    paypal_factory = PayPalFactory()
    paypal_gateway = paypal_factory.create_payment_gateway()
    paypal_gateway.process_payment(100)

    stripe_factory = StripeFactory()
    stripe_gateway = stripe_factory.create_payment_gateway()
    stripe_gateway.process_payment(200)

if __name__ == "__main__":
    main()
