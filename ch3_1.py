def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year%400 == 0)

def day_of_year(day, month ,year) :
    day_of_years = 0
    day_in_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]

    if is_leap(year):
        day_in_month[2] += 1

    if not(1 <= month<= 12):
        return "Invalid"
    
    if not(1 <= day <= day_in_month[month]):
        return "Invalid"
    for i in range(1,month):
        day_of_years += day_in_month[i]
    day_of_years += day
    return day_of_years

day_str = input("Enter a date : ")

try:
    d, m, y = day_str.split("-")
    if y.isdigit():
        leap = is_leap(int(y))
    else:
        leap = "Invalid"

    if not (d.isdigit() and m.isdigit() and y.isdigit()):
        print(f"day of year: Invalid ,is_leap: {leap}")
    else:
        day, month, year = int(d), int(m), int(y)
        print(f"day of year: {day_of_year(day, month, year)} ,is_leap: {leap}")

except:
    print("day of year: Invalid ,is_leap: False")