def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year%400 == 0)

def day_in_year(year):
    if is_leap(year):
        return 366
    else:
        return 365

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

def date_diff(date1_str, date2_str):
    d1, m1, y1 = map(int, date1_str.split('-')) 
    d2, m2, y2 = map(int, date2_str.split('-'))

    if "Invalid Input" in str(day_of_year(d1, m1, y1)):
        return "Invalid"
    if "Invalid Input" in str(day_of_year(d2, m2, y2)):
        return "Invalid"
    
    total_days = 0

    if y1 == y2:
        return day_of_year(d2, m2, y2) - day_of_year(d1, m1, y1) + 1

    days_in_y1 = day_in_year(y1)
    days_remaining_in_y1 = days_in_y1 - day_of_year(d1, m1, y1) + 1
    total_days += days_remaining_in_y1

    for y in range(y1 + 1, y2):
        total_days += day_in_year(y)

    days_in_y2_until_date2 = day_of_year(d2, m2, y2)
    total_days += days_in_y2_until_date2
    
    return total_days
date1_str,date2_str = [str(e) for e in input("Enter Input: ").split(",")]
diff_total = date_diff(date1_str, date2_str)
print(f"{diff_total}")