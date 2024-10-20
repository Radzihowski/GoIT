from faker import Faker
from connect import run_query

fake = Faker('uk_UA')


def fill_positions(n: int):
    for i in range(1, n + 1):
        name = fake.name()
        city = fake.city_name()
        sql = '''
            INSERT INTO cities (name, city) VALUES(%s, %s);
        '''
        run_query(sql, (name, city))


if __name__ == '__main__':
    fill_positions(100000)
