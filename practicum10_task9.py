import datetime

def date_time_del(possible_date: str) -> float:
    """Return difference between one date and start of the year"""
    try:
        date, time = possible_date.split()
        month, day, year = map(int, date.split('/'))
        hour, minute, second = map(int, time.split(':'))
    except ValueError:
        raise ValueError("Неверный формат ввода")

    earlier_time = datetime.datetime(year, 1,1, 0, 0, 0)
    later_time = datetime.datetime(year, month, day, hour, minute, second)
    difference = later_time - earlier_time
    seconds = difference.total_seconds()

    return seconds

















