class Money:
    EXCHANGE_RATE = {"AMD": 1, "RUB": 4, "USD": 400, "EUR": 420}

    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __repr__(self):
        return "{} {}".format(self.amount, self.currency)

    def exchange(self, curr):
        rate = Money.EXCHANGE_RATE[self.currency] / Money.EXCHANGE_RATE[curr]
        return Money(curr, rate * self.amount)

    def __add__(self, other):
        if self.currency != other.currency:
            other = other.exchange(self.currency)
        return Money(self.currency, self.amount + other.amount)

    def __mul__(self, n):
        return Money(self.currency, self.amount * n)



