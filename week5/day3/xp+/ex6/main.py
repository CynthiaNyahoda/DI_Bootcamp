from datetime import datetime

def minutes_lived(birthdate):
    now = datetime.now()
    time_lived = now - birthdate
    minutes = int(time_lived.total_seconds() / 60)
    print(f"You have lived for {minutes} minutes.")
birthdate = datetime(1990, 1, 1)
minutes_lived(birthdate)
