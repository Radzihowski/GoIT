import datetime
import numpy as np
import random

from faker import Faker
from itertools import cycle
from connect import run_query

fake = Faker()
SUBJECT_LIST = ["mathematics", "geography", "chemistry", "english", "history"]
START_DATE = datetime.date(2023, 9, 1)
END_DATE = datetime.date(2024, 5, 31)
random.shuffle(SUBJECT_LIST)


def get_ids_by_table(table: str):
    sql = f''' 
                SELECT id FROM {table};
            '''
    result = run_query(sql)
    id_list = [item[0] for item in result]
    return id_list


def api_key_generator(api_keys):
    return (key for key in cycle(api_keys))



def fill_students(n: int):
    group_ids = get_ids_by_table("groups")
    api_key_gen = api_key_generator(group_ids)

    for i in range(1, n + 1):
        first_name = fake.first_name()
        second_name = fake.last_name()
        group_id = next(api_key_gen)
        print(first_name, second_name)
        sql = ''' 
            INSERT INTO students(first_name,second_name,group_id) VALUES(%s,%s,%s);
        '''
        run_query(sql, (first_name, second_name, group_id))

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





def subjects(subject_list: list):
    teachers_ids = get_ids_by_table("teachers")
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


def add_marks(blocks: int):
    students_ids = get_ids_by_table("students")
    print(students_ids)
    subjects_ids = get_ids_by_table("subjects")
    print(subjects_ids)



    for subject_id in subjects_ids:
        for block in range(1, blocks+1):
            date = fake.date_between(start_date=START_DATE, end_date=END_DATE)
            for student_id in students_ids:
                mark = random.randint(1, 10)
                sql = '''
                            INSERT INTO marks (mark, student_id, subject_id, date) VALUES(%s,%s,%s,%s);
                        '''
                run_query(sql, (mark, student_id, subject_id, date))


if __name__ == "__main__":
    fill_groups(3)
    fill_students(50)
    teachers(5)
    subjects(SUBJECT_LIST)
    add_marks(4)
    pass
