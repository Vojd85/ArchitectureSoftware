from interfaces.i_user_repo import IUserRepo
from data_classes.user import User


class UserRepo(IUserRepo):
    def __init__(self):
        self._users: list[User] = []

    def all_users(self):
        return self._users
    
    def create_user(self, user: User):
        self._users.append(user)

    def read_user(self, id: int):
        for user in self._users:
            if user.get_id() == id:
                return user
            
    def delete_user(self, id: int):
        for user in self._users:
            if user.get_id() == id:
                self._users.remove(user)