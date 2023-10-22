from abc import ABC, abstractmethod


class ITicketRepo(ABC):
    @abstractmethod
    def all_tickets():
        pass

    @abstractmethod
    def create_ticket():
        pass

    @abstractmethod
    def read_ticket():
        pass
    
    @abstractmethod
    def update_ticket():
        pass

    @abstractmethod
    def delete_ticket():
        pass