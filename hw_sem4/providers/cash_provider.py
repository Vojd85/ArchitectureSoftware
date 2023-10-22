from interfaces.i_cash_repo import ICashRepo
from repositories.cash_repo import CashRepo
from data_classes.bank_account import BankAccount


class CashProvider:
    def __init__(self):
        self.cash_repo: ICashRepo = CashRepo()

    def create_account(self, card: int, balance: float):
        account = BankAccount(card, balance)
        self.cash_repo.add_account(account)

    def read_account(self, card:int):
        return self.cash_repo.get_account(card)

    def update_balance(self, card:int, value:float):
        for account in self.cash_repo.all_accounts():
            if account.getcard() == card:
                account.set_balance(value)

    def delete_account(self, card:int):
        self.cash_repo.delete_account(card)

    