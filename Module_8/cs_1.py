from datetime import datetime

current_day = datetime.now()
print(current_day)

print(current_day.date())
print(current_day.time())
print(current_day.year, current_day.month, current_day.hour, sep='\t')