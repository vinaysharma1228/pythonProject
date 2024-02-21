def checkLeapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


year=int(input("Enter year : "))

if checkLeapYear(year):
    print(f"{year} is leap year.")
else:
    print(f"{year} is not leap year.")