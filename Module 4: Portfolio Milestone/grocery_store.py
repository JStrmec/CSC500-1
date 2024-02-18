from shopping import ItemtoPurchase

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

def main():
    print("Welcome to the Grocery Store")
    print("Please enter the number of items you want to buy")
    number_of_items = int(input("Enter the number of items: "))
    items = []
    for i in range(number_of_items):
        print(f"Item {i + 1}")
        items.append(add_item())
        print()
    total_cost = total_cost_(items)
    reciept(items, total_cost)

main()