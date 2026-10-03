# Main execution script importing functions from separate modules
from display_menu import display_menu
from take_order import take_order
from calculate_order import calculate_order
from print_receipt import print_receipt

def main():
    menu = {
        "Burger": 80,
        "Chicken": 120,
        "Spaghetti": 100,
        "French Fries": 60,
        "Softdrink": 40
    }

    display_menu(menu)

    want_order = input("\nDo you want to order? (yes/no): ")

    if want_order.lower() == "yes":
        orders = take_order(menu)

        if len(orders) > 0:
            receipt, total = calculate_order(menu, orders)
            print_receipt(receipt, total)
        else:
            print("No order was made.")

    else:
        print("Thank you! Goodbye.")

if __name__ == "__main__":
    main()