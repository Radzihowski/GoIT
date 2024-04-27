# Є список IP адрес:
# IP = [
#     "85.157.172.253",
#     ...
# ]
# Реалізуйте дві функції. Перша get_count_visits_from_ip за допомогою Counter повертатиме словник, де ключ це IP, а значення – кількість входжень у вказаний список.
# Приклад:
# {
#     '85.157.172.253': 2,
#     ...
# }
# Друга функція get_frequent_visit_from_ip повертає кортеж з найбільш часто уживаним в списку IP і кількістю його появ в списку.
# Приклад:
# ('66.50.38.43', 4)

from collections import Counter

def get_count_visits_from_ip(ips):
    entry_counter = {}
    for item in ips:
        if item in entry_counter:
            entry_counter[item] += 1
        else:
            entry_counter[item] = 1
    return entry_counter



def get_frequent_visit_from_ip(ips):
    ip_counter = Counter(ips)
    print(ip_counter.most_common(1))
    most_frequent = ip_counter.most_common(1)
    return most_frequent[0]


print(get_count_visits_from_ip([
    "85.157.172.253",
    "85.157.172.259",
    "85.157.172.253",
    "85.157.172.253",
    "85.157.172.254",
    "85.157.172.255",
    "85.157.172.256",
    "85.157.172.257",
    "85.157.172.258",
    "85.157.172.259"    
]))

print(get_frequent_visit_from_ip([
    "85.157.172.253",
    "85.157.172.259",
    "85.157.172.253",
    "85.157.172.253",
    "85.157.172.254",
    "85.157.172.255",
    "85.157.172.256",
    "85.157.172.257",
    "85.157.172.258",
    "85.157.172.259"    
]))