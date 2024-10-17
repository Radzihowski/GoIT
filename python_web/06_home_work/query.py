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

query_1 =  """
    SELECT AVG(m.mark), s.student_id, s.first_name, s.second_name
    FROM marks AS m
    JOIN 
"""

query_2 =  """
    SELECT m.student_id, AVG(m.mark)
    FROM students st
    JOIN marks as m ON st.id = m.student_id
    WHERE m.subject_id = 1
    ORDER BY m.mark DESC
"""

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
    SELECT AVG(m.mark)
    FROM marks AS m;
"""

query_5 =  """
    SELECT *
    FROM subjects AS s
    WHERE s.teacher_id = 1
"""

query_6 =  """
    SELECT *
    FROM students AS s
    WHERE s.group_id = 1
"""

query_7 =  """
    SELECT m.mark, m.student_id
    FROM marks AS m
    JOIN students AS st ON m.student_id = st.id
    JOIN groups as g ON st.group_id = g.id
    WHERE m.subject_id = 1 AND st.group_id = 1


"""

query_8 =  """

"""

query_9 =  """

"""

query_10 =  """

"""

if __name__ == "__main__":
    # print(run_query(query_1)) doesn't work
    # print(run_query(query_2)) doesn't work
    # print(run_query(query_3))
    # print(run_query(query_4))
    # print(run_query(query_5))
    # print(run_query(query_6))
    print(run_query(query_7))
    # print(run_query(query_8))
    # print(run_query(query_9))
    # print(run_query(query_10))
