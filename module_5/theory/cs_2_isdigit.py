# str.find(substring): Повертає індекс першого входження підрядка substring у строку, або -1, якщо підрядок не знайдено.

articles_dict = [
    {
        "playset": "Semi final voleyball strike",
        "command": "Super Star",
        "year": 1989,
    },
    {
        "playset": "Quater final Finansial competition",
        "command": "Actual price",
        "year": 2020,
    },
    {
        "playset": "Glory speed test call centre of East Erope",
        "command": "Modern Operators",
        "year": 1921,
    },
    {
        "playset": "Endless war From Age of Dragons",
        "command": "Kings of Glory",
        "year": 2012,
    },
]


def find_states(key_word, letter_case=False):
    actual_states = list()
    if letter_case:
        for i in range(len(articles_dict)):
            if articles_dict[i]["playset"].find(key_word) != -1 or \
                    articles_dict[i]["command"].find(key_word) != -1:
                actual_states.append(articles_dict[i])
    else:
        for i in range(len(articles_dict)):
            if (articles_dict[i]["playset"].lower()).find(key_word) != -1 or \
                    (articles_dict[i]["command"].lower()).find(key_word) != -1:
                actual_states.append(articles_dict[i])
        return actual_states


print(find_states("fin"))
print(find_states("age", False))

# print("Endless war From Age of Dragons".find('Ages'))
