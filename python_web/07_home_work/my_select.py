from sqlalchemy import select
from db import session
from models import Student, Teacher, Subject, Group, Mark
from sqlalchemy import and_, or_, not_, func
from pprint import pprint
def select_1():
    ...
def select_2():
    ...
def select_3():
    ...
def select_4():
    ...
def select_5(teacher_id:int):
    """Знайти які курси читає певний викладач."""
    stmt = select(Subject).join(Teacher).where(Teacher.id == teacher_id)
    result = session.execute(stmt).scalars().all()
    # result2 = [[ i.teacher.fullname, i.name ] for i in result]
    return [ i.name for i in result]

def select_6(group_id:int):
    """Знайти список студентів у певній групі."""
    stmt = select(Student).join(Group).where(Group.id == group_id)
    result = session.execute(stmt).scalars().all()
    return [ i.fullname for i in result ]

def select_7(group_id:int, subject_id:int):
    """Знайти оцінки студентів у окремій групі з певного предмета."""
    stmt = select(Mark).join(Student).join(Group).join(Subject).where(and_(Group.id == group_id),
                                                                      (Subject.id == subject_id))
    result = session.execute(stmt).scalars().all()
    return [[i.student.fullname, i.student.group.name, i.subject.name, i.grade] for i in result]

def select_8(teacher_id:int):
    """Знайти середній бал, який ставить певний викладач зі своїх предметів."""
    stmt = select(func.avg(Mark.grade).label("Avg mark")).join(Subject).join(Teacher).where(Teacher.id == teacher_id).group_by(Subject.id)
    result = session.execute(stmt).scalars().all()
    return [i for i in result]
def select_9():
    ...
def select_10():
    ...

if __name__ == "__main__":
    # select_5(1)
    # select_6(2)
    # pprint(select_7(1, 1))
    pprint(select_8(1))