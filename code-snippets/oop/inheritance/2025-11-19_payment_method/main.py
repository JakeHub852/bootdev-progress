class PaymentMethod:
    def __init__(self, name, percent_fee_bps, fixed_fee_cents):
        # Store the name of the payment method
        self.name = name
        # Store the percentage fee in basis points (e.g., 290 for 2.90%)
        self.percent_fee_bps = percent_fee_bps
        # Store the fixed fee in cents
        self.fixed_fee_cents = fixed_fee_cents

    def calculate_fee(self, amount_cents):
        # If the amount is zero or negative, no fee is applied.
        if amount_cents <= 0:
            return 0
        # Calculate the percentage-based fee using integer division
        # (basis points: 10000 bps = 100%, 100 bps = 1%)
        percent_fee = amount_cents * self.percent_fee_bps // 10000
        # Add the fixed fee to the calculated percentage fee
        total_fee = percent_fee + self.fixed_fee_cents
        # Ensure the total fee is never negative
        if total_fee < 0:
            return 0
        return total_fee


class CreditCard(PaymentMethod):
    def __init__(self, international=False):
        # Initialize the base PaymentMethod with "Credit Card" name,
        # a 2.90% fee (290 bps), and a 30 cent fixed fee.
        # These values come from the lesson's requirements for CreditCard base fees.
        PaymentMethod.__init__(self, "Credit Card", 290, 30)
        # Store whether the transaction is international, which affects the fee.
        self.international = international 
        
    def calculate_fee(self, amount_cents):
        # If the amount is zero or negative, no fee is applied.
        if amount_cents <= 0:
            return 0
        # Get the base fee calculation from the parent PaymentMethod class.
        base_fee = PaymentMethod.calculate_fee(self, amount_cents)
        # If the transaction is international, add an additional 100 cent surcharge.
        # This is a specific rule for CreditCard international transactions.
        if self.international:
            base_fee = base_fee + 100
        # Ensure the final fee is never negative.
        if base_fee < 0:
            return 0
        return base_fee


class BankTransfer(PaymentMethod):
    def __init__(self):
        # Initialize the base PaymentMethod with "Bank Transfer" name,
        # 0% fee (0 bps), and a 25 cent fixed fee.
        # These values come from the lesson's requirements for BankTransfer base fees.
        PaymentMethod.__init__(self, "Bank Transfer", 0, 25)

    def calculate_fee(self, amount_cents):
        # If the amount is zero or negative, no fee is applied.
        if amount_cents <= 0:
            return 0
        # For amounts >= 10000 cents ($100.00), the fee is waived entirely.
        # This is a specific rule for BankTransfer.
        if amount_cents >= 10000:
            return 0
        # Get the fee calculation from the parent PaymentMethod class for other cases.
        fee = PaymentMethod.calculate_fee(self, amount_cents)
        # Ensure the fee is never negative.
        if fee < 0:
            return 0
        return fee


class Crypto(PaymentMethod):
    def __init__(self, network_fee_cents):
        # Initialize the base PaymentMethod with "Crypto" name,
        # 0% fee (0 bps), and a fixed fee equal to the provided network_fee_cents.
        # The network_fee_cents is specific to each Crypto payment instance.
        PaymentMethod.__init__(self, "Crypto", 0, network_fee_cents)
        # Store the network fee for potential later reference (though not strictly used here beyond __init__).
        self.network_fee_cents = network_fee_cents

    def calculate_fee(self, amount_cents):
        # If the amount is zero or negative, no fee is applied.
        if amount_cents <= 0:
            return 0
        # Get the base fee calculation from the parent PaymentMethod class.
        # This will include the network_fee_cents set during initialization.
        fee = PaymentMethod.calculate_fee(self, amount_cents)
        # For amounts >= 5000 cents ($50.00), apply a 25 cent discount on the fee.
        # This is a specific rule for Crypto payments.
        if amount_cents >= 5000:
            fee = fee -  25
        # Ensure the final fee is never negative after the discount.
        if fee < 0:
            return 0
        return fee


def checkout_total_cents(item_prices_cents, payment_method):
    # Initialize subtotal to 0.
    subtotal = 0
    # Sum all the item prices to get the total before fees.
    # This iterates through the list of prices provided.
    for p in item_prices_cents:
        subtotal = subtotal + p
    # Ask the specific payment method instance to calculate its fee based on the subtotal.
    # The payment_method object determines its own fee rules.
    fee = payment_method.calculate_fee(subtotal)
    # Return the final total: subtotal plus the calculated fee.
    return subtotal + fee