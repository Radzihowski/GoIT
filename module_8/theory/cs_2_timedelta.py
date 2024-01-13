# Клас datetime.timedelta - різниця між двома моментами часу, з точністю до мікросекунд.
#
# Розглянемо таке завдання. Наприклад лікар прописала пацієнтові приймати ліки протягом 45 днів. Треба знайти дату
# закінчення приймання ліків від поточної дати.

from datetime import datetime, timedelta

current_day = datetime.now()
print(current_day)
interval = timedelta(days=45)
print(current_day + interval)
day_off = current_day - interval
day_on = current_day + interval
print(day_on - day_off)
