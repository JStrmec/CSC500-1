points = {0:0, 2:5, 4:15, 6:30, 8:60}

def main():
    books_purchased = int(input('Enter the number of books purchased: '))
    if books_purchased < 0:
        print('Invalid input')
    elif books_purchased in points:
        print('You have earned', points[books_purchased], 'points')
    elif books_purchased > 8:
        print('You have earned 60 points')
    else:
        bookspurchased = books_purchased + 1
        print('You have earned', points[bookspurchased]/2, 'points')
main()