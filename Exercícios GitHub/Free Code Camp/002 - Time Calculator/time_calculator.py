from calendar import FRIDAY, MONDAY, SATURDAY, SUNDAY, THURSDAY, TUESDAY, WEDNESDAY


def get_days_later(days):
    """
        Helper function to format days later
    """

    if days == 1:
        return "(next day)"

    elif days > 1:
        return f"{days} days later"
    
    return ""

def add_time(start, duration, day=False):
    week_days = [
        'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY',
        'FRIDAY', 'SATURDAY', 'SUNDAY'
    ]

    days_later = 0
    one_day = 24
    half_day = 12
    hours, mins = start.split(":")
    mins, period = mins.split(" ")
    dh, dm = duration.split(":")

    
    hours = int(hours)  # start hour
    mins = int(mins)  # start min
    dh = int(dh)  # duration hours
    dm = int(dm)  # duration mins
    period = period.strip().lower()


    total_mins = mins + dm
    total_hours = hours + dh

    if total_mins >= 60:
        total_hours += int(total_mins / 60)
        total_mins = int(total_mins % 60)

    if dh or dm:
        if period == "pm" and total_hours > half_day:
            if total_hours % one_day >= 1.0:
                days_later += 1

        if total_hours >= half_day:
            hours_left = total_hours / one_day
            days_later += int(hours_left)

        tth = total_hours
        while True:
            if tth < half_day:
                break
            if tth >= half_day:
                if period == "am":
                    period = "pm"
                elif period == "pm":
                    period = "am"
                tth -= half_day

    # RE-ADJUST HRS AND MIN
    # Above.. we already taken care of the days
    # so now we need to remove the days from the hrs and keep whats left.
    # EX: hr % oneday -->  55hr % 24 = 7 remaining --> hr=7
    remaining_hours = int(total_hours % half_day) or hours + 1
    remaining_mins = int(total_mins % 60)

    # Format the results 
    results = f'{remaining_hours}:{remaining_mins:02} {period.upper()}'
    if day: # add day of the week
        day = day.strip().lower()
        selected_day = int((week_days.index(day) + days_later) % 7)
        current_day = week_days[selected_day]
        results += f', {current_day.title()} {get_days_later(days_later)}'

    else: # add days later
        results = " ".join((results, get_days_later(days_later)))

    return results.strip()