def ask_number_of_years():
    return int(input('Enter the number of years to calculate rainfall: '))

def ask_inches_of_rainfall(years):
    total = 0.0
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    for year in range(years):
        for month in months:
            total += float(input('Enter the inches rainfall for ' + month + ' year ' + str(year+1) + ': '))
    return total

def main():
    years = ask_number_of_years()
    total = ask_inches_of_rainfall(years)
    months = years * 12
    print('The total rainfall for', months, 'months is', total, 'inches')
    print(f'The average monthly rainfall fo {months:.3f} months is{(total/months):.3f} inches')

main()