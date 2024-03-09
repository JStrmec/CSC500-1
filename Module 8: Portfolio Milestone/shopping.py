from lorem_text import lorem
from enum import Enum

class ItemtoPurchase():
    def __init__(
            self, 
            item_name: str = "none",
            item_description: str = lorem.sentence(), 
            item_price: int = 0, 
            item_quantity: int = 0
        ) -> None:
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.description = item_description

    def print_item_cost(self) -> None:
        print(f"""{self.item_name} {self.item_quantity} @ 
              ${self.item_price:.2f} = $
              {(self.item_price * self.item_quantity):.2f}""")

class ShoppingCart():
    def __init__(self, 
            customer_name: str = "none", 
            current_date: str = "January 1, 2020"
        ) -> None:
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []
        print(f"Customer name: {self.customer_name}")
        print(f"Today's date: {self.current_date}")

    def get_item(self, item_name: str = "none") -> str:
        for item in self.cart_items:
            if item.item_name == item_name:
                return item
        return f"Item {item_name} does not exist in cart."

    def add_item(self, 
            itemtoPurchase: ItemtoPurchase = None
        ) -> None:
        self.cart_items.append(itemtoPurchase)

    def remove_item(self, item_name: str = "") -> None:
        for item in self.cart_items:
            if item.item_name == item_name:
                
                self.cart_items.remove(item)
                return 
        print("Item not found in cart. Nothing removed.")

    class ModifyChoice(str, Enum):
        PRICE = 'p'
        QUANTITY = 'q'
        DESCRIPTION = 'd'

    def modify_item(self, 
            itemtoPurchase: ItemtoPurchase = None,
            modify_choice:  ModifyChoice = ModifyChoice.PRICE
        ) -> None:
        if modify_choice == self.ModifyChoice.PRICE:
            itemtoPurchase.item_price = int(input("Enter the new price: "))
        elif modify_choice == self.ModifyChoice.QUANTITY:
            itemtoPurchase.item_quantity = int(input("Enter the new quantity: "))
        elif modify_choice == self.ModifyChoice.DESCRIPTION:
            itemtoPurchase.description = input("Enter the new description: ")
        else:
            print("Invalid option")

    def get_num_items_in_cart(self) -> int:
        return len(self.cart_items)
    
    def print_total(self) -> None:
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

    def print_cart(self) -> None:
        print("OUTPUT SHOPPING CART")
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        print()
        for item in self.cart_items:
            item.print_item_cost()
        total_cost = self.get_cost_of_cart()
        print()
        print(f"Total: ${total_cost:.2f}")

    def print_description(self) -> None:
        print("OUTPUT ITEMS' DESCRIPTIONS")
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print()
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.description}")
