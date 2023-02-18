from datetime import datetime

def time_until_january_first():
    now = datetime.now()
    january_first = datetime(now.year + 1, 1, 1)
    time_left = january_first - now
    print(f"The 1st of January is in {time_left.days} days and {time_left.seconds // 3600}:{(time_left.seconds // 60) % 60}:{time_left.seconds % 60} hours.")
time_until_january_first()