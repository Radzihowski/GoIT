from datetime import datetime, timedelta

current_day = datetime.now()
print(current_day)
interval = timedelta(days=45)
print(current_day + interval)
day_off = current_day - interval
day_on = current_day + interval
print(day_on - day_off)
