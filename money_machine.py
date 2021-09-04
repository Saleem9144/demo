class MoneyMachine:

    CURRENCY = "$"

    COIN_VALUES = {
        "Two Dollar": 2,
        "One Dollar": 1,
        "Fifty Cent": 0.50
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"Total revenue: {self.CURRENCY}{self.profit:.2f}\n")

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("COINS only should be inserted into the coffee maker.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change:.2f} in change, making your coffee...")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.\n")
            self.money_received = 0
            return False
