from interfaces.i_ticket_repo import ITicketRepo
from data_classes.ticket import Ticket


class TicketRepo(ITicketRepo):
    def __init__(self):
        self._tickets: list[Ticket] = []

    def all_tickets(self):
        return self._tickets
    
    def create_ticket(self, ticket: Ticket):
        self._tickets.append(ticket)

    def read_ticket(self, id: int):
        for ticket in self._tickets:
            if ticket.get_id() == id:
                return ticket
            
    def update_ticket(self, id: int, valid: bool):
        ticket = self.read_ticket(id)
        ticket.set_valid(valid)

    def delete_ticket(self, id: int):
        for ticket in self._tickets:
            if ticket.get_id() == id:
                self._tickets.remove(ticket)