# This class creates the account class that holds each debt account. The information in
# each account is its name, amount, and interest rate
class Account:
    def __init__(self, name, amount, rate):
        self.name = name
        self.amount = amount
        self.rate = rate

    # Returns the amount of interest an account will generate
    def interest_payment(self):
        return self.amount * self.rate

    # Takes in a payment and calculates how much debt is left in the account
    # after the payment, and returns it
    def make_payment(self, payment):
        self.amount = (self.amount + self.interest_payment()) - payment
        if self.amount < 0:
            self.amount = 0
        return self.amount

    # Returns the interest rate of the account as a string rounded to two decimal points
    def format_interest(self):
        x = self.interest_payment()
        return "{:.2f}".format(x)
