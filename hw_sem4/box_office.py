from customer import Customer
from providers.cash_provider import CashProvider
from providers.ticket_provider import TicketProvider
from providers.user_provider import UserProvider


class BoxOffice:
    def __init__(self):
        self.cash_provider = CashProvider()
        self.ticket_provider = TicketProvider()
        self.user_provider = UserProvider()

    def sell_ticket(self, buyer: Customer, ticket_id):
        ticket = self.ticket_provider.read_ticket(ticket_id)
        customer_balance = self.cash_provider.read_account(buyer.get_account().get_card()).get_balance()
        if customer_balance < ticket.get_price():
            print("Low Balance")
        else:
            buyer.get_account().set_balance(customer_balance - ticket.get_price())
            buyer.add_ticket(ticket)
            self.ticket_provider.delete_ticket(ticket_id)
            print('Ticked was selled')

    def return_ticket(self, buyer:Customer, ticket_id:int):
        ticket = buyer.get_ticket(ticket_id)
        self.ticket_provider.create_ticket(ticket.get_id(), ticket.get_price(), ticket.get_date())
        buyer.get_account().set_balance(buyer.get_account().get_balance() + ticket.get_price())