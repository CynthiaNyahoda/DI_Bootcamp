from datetime import datetime

def next_holiday():
    today = datetime.today()
    holiday_name = "Independence Day"  # Example holiday name
    holiday_date = datetime(today.year, 7, 4)  # Example holiday date
    if holiday_date < today:
        holiday_date = datetime(today.year + 1, 7, 4)
    time_left = holiday_date - today
    print(f"Today's date is {today}. The next holiday is {holiday_name}, which is in {time_left.days} days and {time_left.seconds // 3600}:{(time_left.seconds // 60) % 60}:{time_left.seconds % 60} hours.")
next_holiday()