from datetime import datetime


class Ticket:
    def __init__(self, id: int, price: float, date: datetime, is_valid: bool):
        self._id = id
        self._price = price
        self._datetime = date
        self._valid = is_valid

    def get_id(self):
        return self._id
    
    def get_price(self):
        return self._price
    
    def get_date(self):
        return self._datetime
    
    def is_valid(self):
        return self._valid
    
    def set_valid(self, valid: bool):
        self._valid = valid