from datetime import datetime

birth_day = datetime(1982, 10, 8)
res = datetime.now() - birth_day
print(res)