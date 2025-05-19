from datetime import datetime, date, time, timedelta

# 1. Get current local time
now = datetime.now()
print("Current local datetime:", now)


# 2. Create a specific date
birth_date = date(2009, 7, 25)
print("Custom date (e.g., your birthdate):", birth_date)

# 3. Create a specific time
custom_time = time(14, 30, 15)
print("Custom time:", custom_time)

# 4. Combine date and time
combined = datetime.combine(birth_date, custom_time)
print("Combined datetime:", combined)

# 5. Replace parts of a datetime
modified = now.replace(year=2030, month=12)
print("Modified datetime (changed year/month):", modified)

# 6. Convert string to datetime
date_str = input("Enter a date in DD-MM-YYYY format: ")
try:
    parsed_date = datetime.strptime(date_str, "%d-%m-%Y")
    print("Parsed datetime object:", parsed_date)
except ValueError:
    print("Invalid format! Please use DD-MM-YYYY.")


# 9. Get time difference
past_date = datetime(2009, 7, 25)
difference = now - past_date
print(f"Days since 25th july 2009: {difference.days} days")

# 10. Add/subtract time
one_week_later = now + timedelta(weeks=1)
three_days_ago = now - timedelta(days=3)
print("One week from now:", one_week_later)
print("Three days ago:", three_days_ago)

# 11. From timestamp
import time as t
timestamp = t.time()
dt_from_timestamp = datetime.fromtimestamp(timestamp)
print("Datetime from UNIX timestamp:", dt_from_timestamp)


#--------------------------output--------------------------#
# Current local datetime: 2025-05-19 02:24:14.926578
# Custom date (e.g., your birthdate): 2009-07-25
# Custom time: 14:30:15
# Combined datetime: 2009-07-25 14:30:15
# Modified datetime (changed year/month): 2030-12-19 02:24:14.926578
# Enter a date in DD-MM-YYYY format: 25-07-2009
# Parsed datetime object: 2009-07-25 00:00:00
# Days since 25th july 2009: 5777 days
# One week from now: 2025-05-26 02:24:14.926578
# Three days ago: 2025-05-16 02:24:14.926578
# Datetime from UNIX timestamp: 2025-05-19 02:24:26.056225