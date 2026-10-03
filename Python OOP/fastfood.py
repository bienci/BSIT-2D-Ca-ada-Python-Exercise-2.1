# Class definition holding data and operational methods
class FastFoodSystem:
    def __init__(self):
        # Menu stored as an instance attribute
        self.menu = {
            "Burger": 80,
            "Chicken": 120,
            "Spaghetti": 100,
            "French Fries": 60,
            "Softdrink": 40
        }
        # Orders list encapsulated inside the class instance
        self.orders = []

    def display_menu(self):
        print("\n===== FAST FOOD MENU =====")
        number = 1
        for item, price in self.menu.items():
            print(number, ".", item, "- P", price)
            number += 1

    def take_order(self):
        while True:
            item_name = input("\nEnter menu item: ")

            if item_name in self.menu:
                quantity = int(input("Enter quantity: "))

                self.orders.append([item_name, quantity])
                print("Item added to your order.")

            else:
                print("Item not found in the menu.")

            another = input("Do you want to order another item? (yes/no): ")

            if another.lower() == "no":
                break

    def calculate_order(self):
        total = 0
        receipt = []

        for order in self.orders:
            item_name = order[0]
            quantity = order[1]
            price = self.menu[item_name]
            item_total = price * quantity

            receipt.append([item_name, quantity, price, item_total])
            total += item_total

        return receipt, total

    def print_receipt(self, receipt, total):
        print("\n========== RECEIPT ==========")
        print("Item\t\tQty\tPrice\tTotal")

        for order in receipt:
            print(order[0], "\t\t", order[1], "\tP", order[2], "\tP", order[3])

        print("-----------------------------")
        print("TOTAL: P", total)
        print("=============================")