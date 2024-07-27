def add_time(start: str, duration: str, day=None) -> str:
    DAY_OF_WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    new_time = []
    index = 0

    # Split the start time
    minute_start = int(start.split(':')[1].split()[0])
    hour_start = int(start.split(':')[0])
    period_start = start.split()[1]

    minute_duration = int(duration.split(':')[1])
    hour_duration = int(duration.split(':')[0])

    # Calculate the new time
    if period_start == 'PM':
        hour_start += 12

    new_minute = minute_start + minute_duration
    minute = new_minute % 60
    new_hour = hour_start + hour_duration + new_minute // 60
    hour = new_hour % 24
    day_passed = new_hour // 24

    for day_of_week in DAY_OF_WEEK:
        if day is not None and day_of_week.lower() == day.lower():
            day = day_of_week
            index = DAY_OF_WEEK.index(day_of_week)
            break

    index = (index + day_passed) % 7 if day is not None else 0
    # Modified day
    if hour > 12:
        new_time.append(str(hour - 12))
    elif hour == 0:
        new_time.append(str(12))
    else:
        new_time.append(str(hour))
    new_time.append(':')
    new_time.append(str(minute).rjust(2, '0'))
    new_time.append(' PM' if hour >= 12 else ' AM')
    if day is not None:
        new_time.append(f', {DAY_OF_WEEK[index]}')

    if day_passed == 1:
        new_time.append(' (next day)')
    elif day_passed > 1:
        new_time.append(f' ({day_passed} days later)')

    return ''.join(new_time)


if __name__ == '__main__':
    print(add_time('3:30 PM', '2:12'))  # '5:42 PM'.
    print(add_time('11:55 AM', '3:12'))  # '3:07 PM'.
    print(add_time('2:59 AM', '24:00'))  # '2:59 AM' (next day).
    print(add_time('11:59 PM', '24:05'))  # '12:04 AM' (2 days later).
    print(add_time('8:16 PM', '466:02'))  # '6:18 AM' (20 days later).
    print(add_time('3:30 PM', '2:12', 'Monday'))  # '5:42 PM, Monday'.
    print(add_time('2:59 AM', '24:00', 'saturDay'))  # '2:59 AM, Sunday'.
    print(add_time('11:59 PM', '24:05', 'Wednesday'))  # '12:04 AM, Friday'.
    print(add_time('8:16 PM', '466:02', 'tuesday'))  # '6:18 AM, Monday'.
