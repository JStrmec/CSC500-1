
def tip(cost):
    return cost*0.18

def sales_tax(cost):
    return cost*0.07

def main():
    total_cost = 0.0
    cost_of_food = float(input("Please input the cost of your meal: $"))
    your_tip = tip(cost_of_food)
    tax = sales_tax(cost_of_food)
    total_cost = cost_of_food + your_tip + tax
    print(f"Your 18% Tip is ${your_tip:.2f}")
    print(f"Your 7% Sales Tax is ${tax:.2f}")
    print(f"Your Total Cost is ${total_cost:.2f}")

main()