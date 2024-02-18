from shopping import ItemtoPurchase, ShoppingCart

def add_item():
    item_name = input("Enter the item name: ")
    item_price = float(input("Enter the item price: "))
    item_quantity = int(input("Enter the item quantity: "))
    return ItemtoPurchase(item_name, item_price, item_quantity)

def total_cost_(items):
    total_cost = 0
    for item in items:
        total_cost += item.item_price * item.item_quantity
    return total_cost

def reciept(items, total_cost):
    print("RECIEPT")
    print("TOTAL COST")
    for item in items:
        item.print_item_cost()
    print(f"Total: ${total_cost:.2f}")

def menu_choice(ShopppingCart, choice):
    if choice == 'a':
        ShopppingCart.add_item(add_item())
    elif choice == 'r':
        item_name = input("Enter the item name: ")
        ShopppingCart.remove_item(item_name)
    elif choice == 'c':
        item_name = input("Enter the item name: ")
        item_quantity = int(input("Enter the new quantity: "))
        ShopppingCart.modify_item(ItemtoPurchase(item_name, 0, item_quantity))  
    elif choice == 'i':
        print("OUTPUT ITEMS' DESCRIPTIONS")
        for item in ShopppingCart.cart_items:
            print(f"{item.item_name}: {item.item_description}")
    elif choice == 'o':
        print("OUTPUT SHOPPING CART")
        ShopppingCart.print_cart()
    elif choice == 'q':
        return False
    else:
        print("Invalid option")
    print_menu(ShopppingCart)

def print_menu(ShopppingCart):
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")
    continue_ = input('Choose an option:')
    menu_choice(ShopppingCart, choice)


def main():
    print("Welcome to the Grocery Store")
    customer_name = input("Enter your name: ")
    current_date = input("Enter the current date: ")
    ShopppingCart = ShoppingCart(customer_name)
    print_menu(ShopppingCart)
main()