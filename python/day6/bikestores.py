class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id


class Order:
    def __init__(self, order_id, item_name):
        self.order_id = order_id
        self.item_name = item_name


class Transaction:
    def __init__(self, transaction_id, date, time, order_id, customer_id):
        self.transaction_id = transaction_id
        self.date = date
        self.time = time
        self.order_id = order_id
        self.customer_id = customer_id
