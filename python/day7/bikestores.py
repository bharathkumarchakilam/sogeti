class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id


class Order(Customer):
    def __init__(self, name, customer_id, order_id, item_name):
        super().__init__(name, customer_id)
        self.order_id = order_id
        self.item_name = item_name


class Transaction(Order):
    def __init__(self, name, customer_id, order_id, item_name, transaction_id, date, time):
        super().__init__(name, customer_id, order_id, item_name)
        self.transaction_id = transaction_id
        self.date = date
        self.time = time
        
def get_input():
    return input("Is there any transaction (y/n): ")

def main():
    transactions = []  # List to store all transaction objects
    detail = get_input()

    while detail == 'y' or detail == 'Y':
        name = input("Enter customer name: ")
        customer_id = (input("Enter customer ID: "))
        order_id = (input("Enter order ID: "))
        item_name = input("Enter item name: ")
        transaction_id = (input("Enter transaction ID: "))
        date = input("Enter transaction date (YYYY-MM-DD): ")
        time = input("Enter transaction time (HH:MM AM/PM): ")

        transaction = Transaction(name, customer_id, order_id, item_name, transaction_id, date, time)
        transactions.append(transaction)
        
        detail = get_input()

    print("\nTransaction Details:")
    for transaction in transactions:
        print(f"\nTransaction ID: {transaction.transaction_id}")
        print(f"Customer: {transaction.name} (ID: {transaction.customer_id})")
        print(f"Item: {transaction.item_name} (Order ID: {transaction.order_id})")
        print(f"Date: {transaction.date}, Time: {transaction.time}")
        print()
    
    print("There are no more transactions.")

main()
