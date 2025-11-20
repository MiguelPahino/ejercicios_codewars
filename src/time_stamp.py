def time_stamp(dt):
    year, month, day, hour, minute, second = dt

    def is_leap_year(y):
        return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)

    days = 0
    for y in range(1970, year):
        days += 366 if is_leap_year(y) else 365

    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        days_in_month[1] = 29

    days += sum(days_in_month[:month - 1]) + (day - 1)
    total_seconds = days * 86400 + hour * 3600 + minute * 60 + second

    return total_seconds


if __name__ == "__main__":

    assert time_stamp((1970, 1, 1, 0, 0, 0)) == 0
    assert time_stamp((1970, 1, 1, 0, 0, 1)) == 1
    assert time_stamp((1970, 1, 2, 0, 0, 0)) == 86400

 