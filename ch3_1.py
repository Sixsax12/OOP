def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year%400 == 0)

def day_of_year(day, month ,year) :
    day_of_years = 0
    day_in_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]

    if is_leap(year):
        day_in_month[2] += 1

    if not(1 <= month<= 12):
        return "Invalid Input"
    
    if not(1 <= day <= day_in_month[month]):
        return "Invalid Input"
    for i in range(1,month):
        day_of_years += day_in_month[i]
    day_of_years += day
    return day_of_years
day,month,year = [int(e) for e in input("Input : ").split(",")]
print(f"29/2/2023 (Not Leap): {day_of_year(day, month, year)}")