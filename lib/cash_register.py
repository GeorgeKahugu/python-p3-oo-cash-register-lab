#!/usr/bin/env python3

# class CashRegister:
#   def __init__(self, discount=0):
#     self.total=0
#     self.discount = discount
#     self.items = []
#   pass


# class CashRegister:
#     def __init__(self, discount=0):
#         self.total = 0
#         self.discount = discount
#         self.items = []

#     def add_item(self, title, price, quantity=1):
#         for _ in range(quantity):
#             self.items.append(title)
#             self.total += price

#     def apply_discount(self):
#         if self.discount > 0:
#             self.total -= (self.total * self.discount) / 100
#             print(f"After the discount, the total comes to ${self.total:.2f}.")
#         else:
#             print("There is no discount to apply.")

#     def void_last_transaction(self):
#         if self.items:
#             last_price = self.total
#             last_item = self.items.pop()
#             self.total -= last_price
#             print(f"Removed {last_item} from the transaction. New total is ${self.total:.2f}.")
#         else:
#             print("There are no transactions to void.")


class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []
        self.previous_transactions = []

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity
        for _ in range(quantity):
            self.items.append(item)
        self.previous_transactions.append(
            {"item": item, "quantity": quantity, "price": price}
        )    
            
    def apply_discount(self):
        if self.discount:
            self.total = int(self.total *((100 - self.discount) / 100))
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if not self.previous_transactions:
           return "There are no transactions to void"
        self.total -= (
            self.previous_transactions[-1]["price"]
            *self.previous_transactions[-1]["quantity"]
        )
        for _ in range(self.previous_transactions[-1]["quantity"]):
          self.items.pop()
        self.previous_transactions.pop()





