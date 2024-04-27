from collections import defaultdict

phone_numbers = []

phone_operator_numbers = defaultdict(list)

for ph in phone_numbers:
    if ph.startwith('050') or ph.startwith('095')