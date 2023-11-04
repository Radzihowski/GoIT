string = "Нільс Бор народився в родині професора фізіології Копенгагенського університету Християна Бора (1858—1911) й' \
         'Еллен Адлер (1860—1930). Батьки Бора одружилися 1881 року.Батька Нільса Бора двічі висували кандидатом на" \
         "Нобелівську премію з фізіології або медицини[12]. Мати була донькою" \
         "впливового та вельми заможного єврейського банкіра і парламентаря-ліберала Давида Баруха Адлера[da] (1826—1878)" \
         "і Дженні" \
         "Рафаел (1830—1902) із британської єврейської банкірської династії Raphael Raphael & sons[en][13]."

def counting_digits(string):
    count = 0
    for element in string:
        if element.isdigit():
            count += 1
    return count

print(counting_digits(string))

def counting_numbers(string):
    count = 0
    position = 0
    nums = []
    while position < len(string):
        if string[position].isdigit():
            num = ''
            while position < len(string) and string[position].isdigit():
                num += string[position]
                position += 1
            nums.append(num)
            count += 1
        else:
            position += 1
    return count, nums

print(counting_numbers(string ))

