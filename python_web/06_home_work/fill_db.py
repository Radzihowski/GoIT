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

def fill_groups(n: int):
    for i in range(1,n+1):
        name_of_the_group = "LA"+str(i)
        print(name_of_the_group)
        # sql = '''
        #             INSERT INTO students(LA01,LA02,LA03) VALUES(%s,%s,%s);
        #         '''

if __name__ == "__main__":
    # fill_students(5)
    fill_groups(3)
