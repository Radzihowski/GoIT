# Знайти індекс колонки для excel таблиці
def index_table(column_name: str) -> int:
    index = 0
    for item, char in enumerate(reversed(column_name)):
        index += (ord(char) - 64) * (26 ** item)
    return index

print(index_table('AAA'))