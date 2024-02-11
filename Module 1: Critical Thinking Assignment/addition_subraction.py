def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def main():
    print("Please input an integer, x=", end=" ")
    user_input_x = int(input())
    print("Please input an integer, y=", end=" ")
    user_input_y = int(input())
    print(f"{user_input_x} plus {user_input_y} equals {add(user_input_x,user_input_y)}")
    print(f"{user_input_x} minus {user_input_y} equals {subtract(user_input_x,user_input_y)}")

main()