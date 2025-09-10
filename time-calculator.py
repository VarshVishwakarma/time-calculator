def add_time(start, duration, day=None):
    # Days of the week in proper order
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Parse start time
    time, period = start.split()
    start_hour, start_minute = map(int, time.split(":"))

    # Convert start time to 24-hour format for easier calculation
    if period == "PM" and start_hour != 12:
        start_hour += 12
    if period == "AM" and start_hour == 12:
        start_hour = 0

    # Parse duration
    dur_hour, dur_minute = map(int, duration.split(":"))

    # Add minutes and adjust
    end_minute = start_minute + dur_minute
    extra_hour = end_minute // 60
    end_minute = end_minute % 60

    # Add hours
    total_hours = start_hour + dur_hour + extra_hour

    # Count days passed
    days_later = total_hours // 24
    end_hour_24 = total_hours % 24

    # Convert back to 12-hour format
    if end_hour_24 == 0:
        end_hour = 12
        period = "AM"
    elif end_hour_24 < 12:
        end_hour = end_hour_24
        period = "AM"
    elif end_hour_24 == 12:
        end_hour = 12
        period = "PM"
    else:
        end_hour = end_hour_24 - 12
        period = "PM"

    # Format minutes
    end_minute = str(end_minute).rjust(2, "0")

    # Start building result
    new_time = f"{end_hour}:{end_minute} {period}"

    # Handle day of week
    if day:
        day_index = days_of_week.index(day.capitalize())
        new_day_index = (day_index + days_later) % 7
        new_day = days_of_week[new_day_index]
        new_time += f", {new_day}"

    # Handle days later
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time

# Example test cases
print(add_time("3:00 PM", "3:10"))
print(add_time("11:30 AM", "2:32", "Monday"))
print(add_time("10:10 PM", "3:30"))
print(add_time("11:43 PM", "24:20", "Tuesday"))
print(add_time("6:30 PM", "205:12"))
