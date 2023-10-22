from data_classes.user import User
from data_classes.ticket import Ticket
from data_classes.bank_account import BankAccount


class Customer(User):
    def __init__(self, id: int, name: str, passwrd: str, bank_account: BankAccount):
        super().__init__(id, name, passwrd, bank_account)
        self._tickets: list[Ticket] = []

    def get_tickets(self):
        return self._tickets
    
    def add_ticket(self, ticket:Ticket):
        self._tickets.append(ticket)

    def get_ticket(self, id:int):
        for ticket in self._tickets:
            if ticket.get_id() == id:
                return ticket

    def delete_ticket(self, id:int):
        for ticket in self._tickets:
            if ticket.get_id() == id:
                self._tickets.remove(ticket)

