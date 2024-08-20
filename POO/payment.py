from abc import ABC, abstractmethod

# Clase abstracta que define la estructura de un pago
class Payment(ABC):
    def __init__(self, amount):
        self.amount = amount

    # Método abstracto que debe ser implementado por las clases derivadas
    @abstractmethod
    def process_payment(self):
        pass

    def payment_details(self):
        return f"Processing payment of ${self.amount}"

# Clase derivada para pagos con tarjeta de crédito
class CreditCardPayment(Payment):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number

    def process_payment(self):
        details = super().payment_details()
        return f"{details} using Credit Card ending in {self.card_number[-4:]}."

# Clase derivada para pagos con PayPal
class PayPalPayment(Payment):
    def __init__(self, amount, email):
        super().__init__(amount)
        self.email = email

    def process_payment(self):
        details = super().payment_details()
        return f"{details} using PayPal account {self.email}."

# Uso de las clases
credit_card_payment = CreditCardPayment(100, "1234567812345678")
print(credit_card_payment.process_payment())

paypal_payment = PayPalPayment(200, "user@example.com")
print(paypal_payment.process_payment())
