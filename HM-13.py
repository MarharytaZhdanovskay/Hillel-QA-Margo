"""
Hometask 13. class

Task description:
write class for bank card.
Class should reflect card lifecycle, card operations etc.
use CVV, PIN, Name, Surname , end date, card_num as initial params
class should have in addition to common logic some class attributes,
as minimum one classmethod and
as minimum  one staticmethod, two or more getters/setters
do not forget about block \"""if __name__ == '__main__': \"""
"""


import datetime


class BankCard:
    def __init__(self, card_num, cvv, pin, name, surname, end_date):
        self.card_num = card_num
        self.cvv = cvv
        self.pin = pin
        self.name = name
        self.surname = surname
        self.end_date = end_date
        self.is_blocked = False

    @classmethod
    def generate_expiry_date(cls):
        today = datetime.date.today()
        expiry_date = today.replace(year=today.year + 3)
        return expiry_date

    @staticmethod
    def is_valid_card_number(card_num):
        # Add validation logic for card number format
        return len(card_num) == 16

    def block_card(self):
        self.is_blocked = True

    def unblock_card(self):
        self.is_blocked = False

    def is_card_blocked(self):
        return self.is_blocked

    # Getters and setters
    def get_card_num(self):
        return self.card_num

    def set_card_num(self, card_num):
        if self.is_valid_card_number(card_num):
            self.card_num = card_num
        else:
            print("Invalid card number format")

    def get_cvv(self):
        return self.cvv

    def set_cvv(self, cvv):
        self.cvv = cvv

    def get_pin(self):
        return self.pin

    def set_pin(self, pin):
        self.pin = pin

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_surname(self):
        return self.surname

    def set_surname(self, surname):
        self.surname = surname

    def get_end_date(self):
        return self.end_date

    def set_end_date(self, end_date):
        self.end_date = end_date


if __name__ == '__main__':
    # Example usage:
    card = BankCard("1234567890123456", "123", "1234", "Margo", "Test",
                    BankCard.generate_expiry_date())

    print(f"Card Number: {card.get_card_num()}")
    print(f"CVV: {card.get_cvv()}")
    print(f"Name: {card.get_name()} {card.get_surname()}")
    print(f"End Date: {card.get_end_date()}")

    card.set_card_num("9876543210987654")
    card.set_cvv("456")
    card.set_pin("5678")
    card.set_name("Margo")
    card.set_surname("Test2")
    card.set_end_date(BankCard.generate_expiry_date())

    print(f"Updated Card Number: {card.get_card_num()}")
    print(f"Updated CVV: {card.get_cvv()}")
    print(f"Updated Name: {card.get_name()} {card.get_surname()}")
    print(f"Updated End Date: {card.get_end_date()}")
