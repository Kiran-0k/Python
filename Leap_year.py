year = int(input("Enter a year: "))

def isYearLeap(year):
    if year >= 1582: #Georgian Calendar Period
        if (year % 4) == 0: #Leap year
            if (year % 100) == 0: #Not a Leap Year
                if (year % 400) == 0: #Leap year
                    print('Leap Year')
                else:
                    print('Common Year')
            else:
                print('Leap Year')
        else:
            print('Common Year')
    else:
        print("Not within the Gregorian calendar period")

isYearLeap(year)
