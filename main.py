from payment_processing import PayPalFactory, StripeFactory
def main():
    paypal_factory = PayPalFactory()
    paypal_gateway = paypal_factory.create_payment_gateway()
    paypal_gateway.process_payment(100)

    stripe_factory = StripeFactory()
    stripe_gateway = stripe_factory.create_payment_gateway()
    stripe_gateway.process_payment(200)

if __name__ == "__main__":
    main()
