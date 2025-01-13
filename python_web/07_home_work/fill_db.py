import datetime
import numpy as np
import random
from db import session
from models import Group, Student, Teacher, Subject, Mark

from faker import Faker
from itertools import cycle

fake = Faker()
SUBJECT_LIST = ["mathematics", "geography", "chemistry", "english", "history"]
START_DATE = datetime.date(2023, 9, 1)
END_DATE = datetime.date(2024, 5, 31)
random.shuffle(SUBJECT_LIST)


def api_key_generator(api_keys):
    return (key for key in cycle(api_keys))


def fill_groups(n: int):
    """ Create records on table groups """
    for i in range(1, n + 1):
        name_of_the_group = "LA" + str(i)
        print(name_of_the_group)
        new_group = Group(name=name_of_the_group)
        session.add(new_group)
    session.commit()


def fill_students(n: int):
    """ Create records about students """
    group_ids = session.query(Group.id).all()
    print(group_ids)
    api_key_gen = api_key_generator(group_ids)

    for i in range(1, n + 1):
        first_name = fake.first_name()
        second_name = fake.last_name()
        group_id = next(api_key_gen)
        print(first_name, second_name)
        new_student = Student(fullname=first_name + ' ' + second_name, group_id=group_id[0])
        session.add(new_student)
    session.commit()


def teachers(n: int):
    """ Create records about teachers """
    for i in range(1, n):
        gender = np.random.choice(["Mr", "Ms"], p=[0.5, 0.5])
        first_name = fake.first_name_male() if gender == "Mr" else fake.first_name_female()
        second_name = fake.last_name()
        print(first_name, second_name)
        new_teacher = Teacher(fullname=gender + ' ' + first_name + ' ' + second_name)
        session.add(new_teacher)
    session.commit()


def subjects(subject_list: list):
    """ Create records about subjects """
    teachers_ids = session.query(Teacher.id).all()
    i = 0
    for subject in subject_list:
        if i >= len(subject_list) - 1:
            i = 0
        teacher_id = teachers_ids[i]
        i += 1
        new_subject = Subject(name=subject, teacher_id=teacher_id[0])
        print(new_subject)
        session.add(new_subject)
    session.commit()



def add_marks(blocks: int):
    """ Create records about marks """
    students_ids = session.query(Student.id).all()
    print(students_ids)
    subjects_ids = session.query(Subject.id).all()
    print(subjects_ids)

    for subject_id in subjects_ids:
        for block in range(1, blocks+1):
            date = fake.date_between(start_date=START_DATE, end_date=END_DATE)
            for student_id in students_ids:
                mark = random.randint(1, 10)
                new_mark = Mark(grade=mark, date_of=date, student_id=student_id[0], subject_id=subject_id[0])
                session.add(new_mark)
    session.commit()


if __name__ == "__main__":
    fill_groups(3)
    fill_students(60)
    teachers(5)
    subjects(SUBJECT_LIST)
    add_marks(4)
    pass
