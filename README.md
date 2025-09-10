# time-calculator
A simple Python project that adds a duration to a given start time in 12-hour format (AM/PM), with optional support for the day of the week. It handles time rollovers, day changes, and large hour additions.

Input start time in HH:MM AM/PM format

Input duration in HH:MM format (hours can be any number, minutes < 60)

Optional day of the week input (case-insensitive)

Handles:

AM ↔ PM conversions

Day rollover (next day) or (n days later)

Correct calculation of resulting day of the week

add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
