from sqlalchemy import func, desc, select, and_

from models import Teacher, Student, Subject, Mark, Group
from db import session


def select_one():
    """
    Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
    :return: list[dict]
    """
    result = session.query(Student.fullname, func.round(func.avg(Mark.grade), 2).label('avg_grade')) \
        .select_from(Mark).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()
    return result

if __name__ == "__main__":
    print(select_one())