from data_classes.user import User
from data_classes.bank_account import BankAccount
from interfaces.i_user_repo import IUserRepo
from repositories.user_repo import UserRepo



class UserProvider:
    def __init__(self):
        self.user_repo: IUserRepo = UserRepo()

    def create_user(self, id:int, name: str, passwrd: str, bank_account: BankAccount):
        user = User(id=id, name=name, passwrd=passwrd, bank_account=bank_account)
        self.user_repo.create_user(user)

    def read_user(self, id:int):
        return self.user_repo.read_user(id)
    
    def delete_user(self, id:int):
        self.user_repo.delete_user(id)