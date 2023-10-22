from data_classes.bank_account import BankAccount


class User:
    def __init__(self, id: int, name: str, passwrd: str, bank_account: BankAccount):
        self._id = id
        self._name = name
        self._password = passwrd
        self._bank_account = bank_account

    def get_id(self):
        return self._id
    
    def get_name(self):
        return self._name
    
    def set_name(self, name: str):
        self._name = name

    def get_password(self):
        return self._password
    
    def set_password(self, passwrd: str):
        self._password = passwrd

    def get_account(self):
        return self._bank_account
    
    def set_account(self, bank_account: BankAccount):
        self._bank_account = bank_account
