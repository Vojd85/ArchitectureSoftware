from abc import ABC, abstractmethod


class ICashRepo(ABC):
    @abstractmethod
    def add_account():
        pass

    @abstractmethod
    def get_account():
        pass

    @abstractmethod
    def delete_account():
        pass

    @abstractmethod
    def all_accounts():
        pass