from pprint import pprint

from sqlalchemy import and_, func, desc
from sqlalchemy import select

from db import session
from models import Student, Teacher, Subject, Group, Mark


def select_1():
    """Знайти 5 студентів із найбільшим середнім балом з усіх предметів."""
    query = (
        select(
            Student.fullname,
            func.round(func.avg(Mark.grade), 2).label("Avg_marks")
        )
        .join(Mark)
        .group_by(Student.id)
        .order_by(desc(func.avg(Mark.grade)))
        .limit(5)
    )
    result = session.execute(query).all()
    return result

def select_2(subject_id:int):
    """Знайти студента із найвищим середнім балом з певного предмета."""
    query = (
        select(
            Student.fullname,
            func.round(func.avg(Mark.grade), 2).label("Avg_marks")
        )
        .join(Student)
        .join(Subject)
        .where(Subject.id == subject_id)
        .group_by(Student.id)
        .order_by(desc(func.avg(Mark.grade)))
        .limit(1))
    result = session.execute(query).all()
    return [i for i in result]

def select_3(subject_id: int):
    """Знайти середній бал у групах з певного предмета."""
    query = (
        select(
            Group.name,
            func.round(func.avg(Mark.grade), 2).label("Avg_marks")
        )
        .join(Student, Group.id == Student.group_id)  # Join students with their groups
        .join(Mark, Student.id == Mark.student_id)    # Join marks with students
        .join(Subject, Mark.subject_id == Subject.id) # Join subjects with marks
        .where(Subject.id == subject_id)             # Filter by subject
        .group_by(Group.id)                          # Group by group
    )
    result = session.execute(query).all()
    return [i for i in result]

def select_4():
    """Знайти середній бал на потоці (по всій таблиці оцінок)."""
    query = (
        select(
            func.round(func.avg(Mark.grade), 2).label("Avg_marks")
        )
    )
    result = session.execute(query).scalars().all()
    return [i for i in result]

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
    stmt = select(Mark).join(Student).join(Group).join(Subject).where(and_(Group.id == group_id,
                                                                           Subject.id == subject_id))
    result = session.execute(stmt).scalars().all()
    return [[i.student.fullname, i.student.group.name, i.subject.name, i.grade] for i in result]

def select_8(teacher_id:int):
    """Знайти середній бал, який ставить певний викладач зі своїх предметів."""
    stmt = select(func.avg(Mark.grade).label("Avg mark")
                  ).join(Subject).join(Teacher).where(Teacher.id == teacher_id).group_by(Subject.id)
    result = session.execute(stmt).scalars().all()
    return [i for i in result]


def select_9(student_id: int):
    """Знайти список курсів, які відвідує певний студент."""
    query = select(Subject).join(Mark).join(Student).where(Student.id == student_id)
    result = session.execute(query).scalars().all()
    return list(set([i.name for i in result]))


def select_10(student_id, teacher_id):
    """Список курсів, які певному студенту читає певний викладач."""
    query = select(Subject).join(Mark).join(Student).where(and_(Student.id == student_id,
                                                                Subject.teacher_id == teacher_id))
    result = session.execute(query).scalars().all()
    return set([i.name for i in result])


if __name__ == "__main__":
    # pprint(select_1())
    # pprint(select_2(1))
    # pprint(select_3(1))
    pprint(select_4())
    # select_5(1)
    # select_6(2)
    # pprint(select_7(1, 1))
    # pprint(select_8(1))
    # pprint(select_9(2))
    # pprint(select_10(2, 1))
