from lorem_text import lorem

class ItemtoPurchase():
    def __init__(self, item_name = "none", item_price = 0, item_quantity = 0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.description = lorem.sentence()

    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${(self.item_price * self.item_quantity):.2f}")

class ShoppingCart():
    def __init__(self, customer_name = "none", current_date = "January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, itemtoPurchase: ItemtoPurchase = None):
        self.cart_items.append(itemtoPurchase)

    def remove_item(self, item_name: str = ""):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return 
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, itemtoPurchase: ItemtoPurchase = None):
        modify_choicer = 'q' #input("Modify item price, quantity, or description? (p/q/d): ")
        if modify_choicer == 'p':
            itemtoPurchase.item_price = int(input("Enter the new price: "))
        elif modify_choicer == 'q':
            itemtoPurchase.item_quantity = int(input("Enter the new quantity: "))
        elif modify_choicer == 'd':
            itemtoPurchase.description = input("Enter the new description: ")
        else:
            print("Invalid option")

    def get_num_items_in_cart(self) -> int:
        return len(self.cart_items)
    
    def print_total(self):
        if self.get_num_items_in_cart() == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print(f"Number of Items: {self.get_num_items_in_cart()}")
            print()
            for item in self.cart_items:
                item.print_item_cost()
            total_cost = self.get_cost_of_cart()
            print()
            print(f"Total: ${total_cost:.2f}")

    def get_cost_of_cart(self) -> float:
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity
        return total_cost

    def print_cart(self):
        print("OUTPUT SHOPPING CART")
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        print()
        for item in self.cart_items:
            item.print_item_cost()
        total_cost = self.get_cost_of_cart()
        print()
        print(f"Total: ${total_cost:.2f}")

    def print_description(self):
        print("OUTPUT ITEMS' DESCRIPTIONS")
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print()
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.description}")
