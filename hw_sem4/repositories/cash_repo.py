from interfaces.i_cash_repo import ICashRepo
from data_classes.bank_account import BankAccount


class CashRepo(ICashRepo):
    def __init__(self):
        self._bank_accounts: list[BankAccount] = []

    def all_accounts(self):
        return self._bank_accounts
    
    def add_account(self, bank_account: BankAccount):
        self._bank_accounts.append(bank_account)

    def get_account(self, card_number: int):
        for account in self._bank_accounts:
            if account.get_card() == card_number:
                return account
            
    def delete_account(self, card_number:int):
        for account in self._bank_accounts:
            if account.get_card() == card_number:
                self._bank_accounts.remove(account)