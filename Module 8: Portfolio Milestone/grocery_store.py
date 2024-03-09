from shopping import ItemtoPurchase, ShoppingCart

def add_item() -> ItemtoPurchase:
    item_name = get_item()
    item_description = input("Enter the item description: ")
    item_price = float(input("Enter the item price: "))
    item_quantity = int(input("Enter the item quantity: "))
    return ItemtoPurchase(
        item_name=item_name,
        item_description=item_description, 
        item_price=item_price, 
        item_quantity=item_quantity)

def get_item()-> str:
    item_name = input("Enter the item name: ")
    return item_name

def get_item_to_remove() -> str:
    item_name = input("Enter name of item to remove: ")
    return item_name

def total_cost_(items: list[ItemtoPurchase]) -> float:
    total_cost = 0
    for item in items:
        total_cost += item.item_price * item.item_quantity
    return total_cost

def reciept(items: list[ItemtoPurchase], total_cost: float) -> str:
    print("RECIEPT")
    print("TOTAL COST")
    for item in items:
        item.print_item_cost()
    print(f"Total: ${total_cost:.2f}")

def menu_choice(ShopppingCart: ShoppingCart, choice: str) -> None:
    if choice == 'a':
        ShopppingCart.add_item(add_item())
    elif choice == 'r':
        print("REMOVE ITEM FROM CART")
        item_name = get_item_to_remove()
        ShopppingCart.remove_item(item_name)
    elif choice == 'c':
        item_name = get_item()
        ShopppingCart.modify_item(ShopppingCart.get_item(item_name))  
    elif choice == 'i':
        ShopppingCart.print_description()
    elif choice == 'o':
        ShopppingCart.print_cart()
    elif choice == 'q':
        return
    else:
        print("Invalid option")
    print_menu(ShopppingCart)

def print_menu(ShopppingCart) -> None:
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")
    choice = input('Choose an option: ')
    menu_choice(ShopppingCart, choice)


def main() -> None:
    print("Welcome to the Grocery Store")
    customer_name = input("Enter your name: ")
    current_date = input("Enter the current date: ")
    ShopppingCart = ShoppingCart(customer_name=customer_name, current_date=current_date)
    print_menu(ShopppingCart)
main()