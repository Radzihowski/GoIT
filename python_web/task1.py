# Як об’єднати елементи списку з кортежів та інших списків в один список? data = [(1, 2), [3, 4], (5, 6)]

data = [(1, 2), [3, 4], (5, 6)]
result = []

for i in data:
    for k in i:
        result.append(k)
print(result)

# list comprehension
result = [k for i in data for k in i]
print(result)
