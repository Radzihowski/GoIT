from datetime import datetime

current_day = datetime.now()
print(current_day.timestamp())

day_zero = datetime.fromtimestamp(0)
print(day_zero)

print(current_day > day_zero)
test_data = '1970:02:01 January Jan 13 03 59'
print(datetime.strptime(test_data, "%Y:%m:%d %B %b %H %I %M"))
test_data = '1970:02:01 13 03 59'
print(datetime.strptime(test_data, "%Y:%m:%d %H %I %M"))
test_data = '1970:May:01 23 59'
print(datetime.strptime(test_data, "%Y:%B:%d %H %M"))
test_data = '1970:Sep:01 03 59'
print(datetime.strptime(test_data, "%Y:%b:%d %I %M"))