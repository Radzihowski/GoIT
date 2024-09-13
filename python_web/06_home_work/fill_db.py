from faker import Faker
from connect import run_query

fake = Faker()

def fill_students(n: int):
    for i in range(1,n):
        first_name = fake.first_name()
        second_name = fake.last_name()
        print(first_name, second_name)
        sql = ''' 
            INSERT INTO students(first_name,second_name) VALUES(%s,%s);
        '''
        run_query(sql, (first_name, second_name))

if __name__ == "__main__":
    fill_students(5)