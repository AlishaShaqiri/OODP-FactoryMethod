# Payment Processing System

This Python project implements a payment processing system for an e-Commerce platform. It supports multiple payment gateways using the Factory Method design pattern. The system provides flexibility to expand and integrate additional payment gateways seamlessly in the future.

## Overview

An e-Commerce platform requires the ability to process payments through different gateways based on user preferences. Each payment gateway operates differently, hence the need for a flexible system capable of accommodating various payment methods.

## Components

- **main.py**: Contains a simple demonstration in the Main method where different types of payment gateways are instantiated via their respective factories, and payments are processed.
- **payment_processing.py**: Defines the core functionality of the payment processing system, including interfaces, concrete classes, creators, and concrete factories.

## Implementation Details

PaymentGateway Interface
Defines the contract for processing payments.

## PayPal and Stripe Classes

Concrete implementations of the PaymentGateway interface, representing PayPal and Stripe payment gateways, respectively.

## PaymentGatewayFactory Interface
Defines the contract for creating payment gateway instances.

## PayPalFactory and StripeFactory Classes
Concrete implementations of the PaymentGatewayFactory interface, responsible for creating instances of PayPal and Stripe payment gateways.

Example


```python
from payment_processing import PayPalFactory, StripeFactory

def main():
    # Instantiate PayPal payment gateway via its factory
    paypal_factory = PayPalFactory()
    paypal_gateway = paypal_factory.create_payment_gateway()
    paypal_gateway.process_payment(100)

    # Instantiate Stripe payment gateway via its factory
    stripe_factory = StripeFactory()
    stripe_gateway = stripe_factory.create_payment_gateway()
    stripe_gateway.process_payment(200)

if __name__ == "__main__":
    main()
