# Function to handle customer input and taking orders
def take_order(menu):
    orders = []

    while True:
        item_name = input("\nEnter menu item: ")

        if item_name in menu:
            quantity = int(input("Enter quantity: "))

            orders.append([item_name, quantity])
            print("Item added to your order.")

        else:
            print("Item not found in the menu.")

        another = input("Do you want to order another item? (yes/no): ")

        if another.lower() == "no":
            break

    return orders