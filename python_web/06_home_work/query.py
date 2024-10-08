from connect import run_query

# Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
# Знайти студента із найвищим середнім балом з певного предмета.
# Знайти середній бал у групах з певного предмета.
# Знайти середній бал на потоці (по всій таблиці оцінок).
# Знайти які курси читає певний викладач.
# Знайти список студентів у певній групі.
# Знайти оцінки студентів у окремій групі з певного предмета.
# Знайти середній бал, який ставить певний викладач зі своїх предметів.
# Знайти список курсів, які відвідує студент.
# Список курсів, які певному студенту читає певний викладач.

query_3 =  """
    SELECT AVG(m.mark), g.group_name
    FROM marks AS m
    JOIN students AS st ON m.student_id = st.id
    JOIN groups as g ON st.group_id = g.id
    WHERE m.subject_id = 1
    GROUP BY g.id
    ORDER BY g.id
"""

query_4 =  """
    SELECT *
    FROM subjects AS s
    WHERE s.teacher_id = 1
"""

query_5 =  """
    SELECT *
    FROM students AS s
    WHERE s.group_id = 1
"""

if __name__ == "__main__":
    # print(run_query(query_3))
    # print(run_query(query_4))
    print(run_query(query_5))