def is_leap(year: int) -> bool:
    """Check if a year is a leap year"""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def date_time(possible_date: str) -> None:
    """Check if a date is a correct and return in particular format"""
    try:
        date, time = possible_date.split()
        month, day, year = map(int, date.split('/'))
        hour, minute, second = map(int, time.split(':'))
    except ValueError:
        return

    valid_date = False
    day_31_month = [1, 3, 5, 7, 8, 10, 12]
    end_str = ''

    if month in day_31_month and 1 <= day <= 31:
        valid_date = True
    elif (1 <= day <= 30 and month not in day_31_month
          and 1 <= month <= 12 and month != 2):
        valid_date = True
    elif month == 2:
        if is_leap(year) and 1 <= day <= 29:
            valid_date = True
        elif not is_leap(year) and 1 <= day <= 28:
            valid_date = True

    if valid_date:
        if hour in range(12, 24) and minute in range(60) and second in range(60):
            if hour != 12:
                hour -= 12
            ampm = 'PM'
        elif hour in range(12) and minute in range(60) and second in range(60):
            if hour == 0:
                hour = 12
            ampm = 'AM'
        else:
            valid_date = False

    if valid_date:
        print(f"{day:02d}.{month:02d}.{year % 100:02d} {hour:02d}:{minute:02d}:{second:02d} {ampm}")

















