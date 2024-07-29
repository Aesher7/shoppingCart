class ItemToPurchase:
    def __init__(self, name="none", description="none", price=0, quantity=0):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def print_item_cost(self):
        print(f"{self.name} {self.quantity} @ ${self.price} = ${self.price * self.quantity}")

    def print_item_description(self):
        print(f"{self.name}: {self.description}")


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        found = False
        for item in self.cart_items:
            if item.name == item_name:
                self.cart_items.remove(item)
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, item):
        found = False
        for cart_item in self.cart_items:
            if cart_item.name == item.name:
                found = True
                if item.description != "none":
                    cart_item.description = item.description
                if item.price != 0:
                    cart_item.price = item.price
                if item.quantity != 0:
                    cart_item.quantity = item.quantity
                break
        if not found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_quantity = sum(item.quantity for item in self.cart_items)
        return total_quantity

    def get_cost_of_cart(self):
        total_cost = sum(item.price * item.quantity for item in self.cart_items)
        return total_cost

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            print(f"Number of Items: {self.get_num_items_in_cart()}")
            for item in self.cart_items:
                item.print_item_cost()
            print(f"Total: ${self.get_cost_of_cart()}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()


def print_menu(cart):
    menu = """
MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option:
"""
    choice = ''
    while choice != 'q':
        print(menu)
        choice = input().strip()
        if choice == 'a':
            print("ADD ITEM TO CART")
            name = input("Enter the item name:\n")
            description = input("Enter the item description:\n")
            price = int(input("Enter the item price:\n"))
            quantity = int(input("Enter the item quantity:\n"))
            item = ItemToPurchase(name, description, price, quantity)
            cart.add_item(item)
        elif choice == 'r':
            print("REMOVE ITEM FROM CART")
            name = input("Enter name of item to remove:\n")
            cart.remove_item(name)
        elif choice == 'c':
            print("CHANGE ITEM QUANTITY")
            name = input("Enter the item name:\n")
            description = input("Enter the new description:\n")
            price = int(input("Enter the new price:\n"))
            quantity = int(input("Enter the new quantity:\n"))
            item = ItemToPurchase(name, description, price, quantity)
            cart.modify_item(item)
        elif choice == 'i':
            print("OUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()
        elif choice == 'o':
            print("OUTPUT SHOPPING CART")
            cart.print_total()
        elif choice != 'q':
            print("Invalid choice. Please choose again.")

def main():
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    cart = ShoppingCart(customer_name, current_date)
    print(f"\nCustomer name: {cart.customer_name}")
    print(f"Today's date: {cart.current_date}")
    print_menu(cart)

if __name__ == "__main__":
    main()
