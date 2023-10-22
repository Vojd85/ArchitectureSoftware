from box_office import BoxOffice
from customer import Customer
from datetime import datetime

office = BoxOffice()
office.cash_provider.create_account(12345, 111.1)
buyer = Customer(1, "Andy", '123', office.cash_provider.cash_repo.get_account(12345))
print(buyer.get_account().get_balance())
office.ticket_provider.create_ticket(1, 22.3, datetime.now())
office.sell_ticket(buyer, 1)
print(buyer.get_account().get_balance())
