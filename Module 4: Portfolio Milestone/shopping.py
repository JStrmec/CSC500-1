class ItemtoPurchase():
    def __init__(self, item_name = "none", item_price = 0, item_quantity = 0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity:.2f} @ ${self.item_price:.2f} = ${(self.item_price * self.item_quantity):.2f}")