from interfaces.i_ticket_repo import ITicketRepo
from repositories.ticket_repo import TicketRepo
from data_classes.ticket import Ticket
from datetime import datetime


class TicketProvider:
    def __init__(self):
        self.ticket_repo: ITicketRepo = TicketRepo()

    def create_ticket(self, id: int, price: float, date: datetime, is_valid: bool=True):
        ticket = Ticket(id, price, date, is_valid)
        self.ticket_repo.create_ticket(ticket)

    def read_ticket(self, id:int):
        return self.ticket_repo.read_ticket(id)
    
    def update_ticket(self, id:int, is_valid:bool):
        self.ticket_repo.update_ticket(id, is_valid)

    def delete_ticket(self, id:int):
        self.ticket_repo.delete_ticket(id)