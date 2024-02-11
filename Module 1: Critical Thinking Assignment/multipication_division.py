def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

def main():
    print("Please input an integer, num1=", end=" ")
    user_input_x = int(input())
    print("Please input an integer, num2=", end=" ")
    user_input_y = int(input())
    print(f"{user_input_x} times {user_input_y} equals {multiply(user_input_x,user_input_y)}")
    print(f"{user_input_y} divided by {user_input_x} equals {divide(user_input_x,user_input_y)}")

main()