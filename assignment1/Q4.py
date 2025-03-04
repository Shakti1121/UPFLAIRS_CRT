# 4. Check if a year is a leap year
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

year = int(input("Enter a year: "))
print("Leap Year" if is_leap_year(year) else "Not a Leap Year")