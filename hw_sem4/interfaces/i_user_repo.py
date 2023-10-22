from abc import ABC, abstractmethod


class IUserRepo(ABC):
    @abstractmethod
    def all_users():
        pass

    @abstractmethod
    def create_user():
        pass

    @abstractmethod
    def read_user():
        pass

    @abstractmethod
    def delete_user():
        pass