class BankAccount:
    def __init__(self, card: int, balance: float = 0):
        self._card_num = card
        self._balance = balance

    def get_card(self):
        return self._card_num
    
    def set_card(self, new_card_number: int):
        self._card_num = new_card_number
    
    def get_balance(self):
        return self._balance
    
    def set_balance(self, new_balance: float):
        self._balance = new_balance