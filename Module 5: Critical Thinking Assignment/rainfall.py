def ask_number_of_years():
    return int(input('Enter the number of years to calculate rainfall: '))

def ask_inches_of_rainfall(years):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    for year in range(years):
        for month in months:
            total += float(input('Enter the inches rainfall for ' + month + ' ' + str(year+1) + ': '))
    return total

def main()
    total = 0.0
    years = ask_number_of_years()
    total = ask_inches_of_rainfall(years)
    months = years * 12
    print('The total rainfall for', months, 'months is', total, 'inches')
    print('The average monthly rainfall for', months, 'months is', total/months, 'inches')
main()