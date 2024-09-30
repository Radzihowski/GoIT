import numpy as np
import random
from faker import Faker

from connect import run_query

fake = Faker()
SUBJECT_LIST = ["mathematics", "geography", "chemistry", "english", "history"]
random.shuffle(SUBJECT_LIST)


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
        sql = '''
                    INSERT INTO groups(group_name) VALUES(%s);
                '''
        run_query(sql, (name_of_the_group,))


def teachers(n: int):
    for i in range(1, n):
        gender = np.random.choice(["Mr", "Ms"], p=[0.5, 0.5])
        first_name = fake.first_name_male() if gender == "Mr" else fake.first_name_female()
        second_name = fake.last_name()
        print(first_name, second_name)
        sql = ''' 
            INSERT INTO teachers(title, first_name,second_name) VALUES(%s,%s,%s);
        '''
        run_query(sql, (gender, first_name, second_name))


def getteachers_ids():
    sql = ''' 
                SELECT id FROM teachers;
            '''
    result = run_query(sql)
    id_list = [item[0] for item in result]
    return id_list


def subjects(subject_list: list):
    teachers_ids = getteachers_ids()
    i = 0
    for subject in subject_list:
        if i >= len(subject_list)-1:
            i = 0
        teacher_id = teachers_ids[i]
        i+=1
        print(teacher_id)
        sql = '''
            INSERT INTO subjects(title, teacher_id) VALUES(%s,%s);
        '''
        run_query(sql, (subject, teacher_id))

if __name__ == "__main__":
    # fill_students(5)
    # fill_groups(3)
    # teachers(5)
    # getteachers_ids()
    subjects(SUBJECT_LIST)
