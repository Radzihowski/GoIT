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
 SELECT st.first_name, round(avg(m.mark), 2) AS avg_grade
    FROM marks m
    RIGHT JOIN students AS st ON st.id = m.student_id
    GROUP BY st.id
    ORDER BY avg_grade DESC
    LIMIT 5;
"""

query_2 =  """
    SELECT st.first_name, st.second_name, AVG(m.mark)
    FROM students st
    RIGHT JOIN marks as m ON st.id = m.student_id
    WHERE m.subject_id = 1
    GROUP BY st.id
    ORDER BY AVG(m.mark) DESC
    LIMIT 1
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

# Знайти оцінки студентів у окремій групі з певного предмета.
query_7 =  """
    SELECT st.first_name, st.second_name, m.mark
    FROM marks AS m
    RIGHT JOIN students AS st ON m.student_id = st.id
    WHERE st.group_id = 1 AND m.subject_id = 1


"""

# Знайти середній бал, який ставить певний викладач зі своїх предметів.
query_8 =  """
    SELECT t.first_name, t.second_name, AVG(m.mark), s.title
    FROM marks AS m
    RIGHT JOIN subjects AS s ON m.subject_id = s.id
    RIGHT JOIN teachers AS t ON s.teacher_id = t.id
    WHERE t.id = 1
    GROUP BY s.id, t.id
"""
# Знайти список курсів, які відвідує студент.
query_9 =  """
    SELECT DISTINCT(sub.title), s.first_name, s.second_name
    FROM marks AS m
    RIGHT JOIN students AS s ON m.student_id = s.id
    RIGHT JOIN subjects AS sub ON m.subject_id = sub.id
    WHERE s.id = 11  
"""

# Список курсів, які певному студенту читає певний викладач.
query_10 =  """
    SELECT DISTINCT(sub.title), s.first_name, s.second_name, t.first_name, t.second_name
    FROM marks AS m
    RIGHT JOIN students AS s ON m.student_id = s.id
    RIGHT JOIN subjects AS sub ON m.subject_id = sub.id
    RIGHT JOIN teachers AS t ON sub.teacher_id = t.id
    WHERE s.id = 1 AND sub.teacher_id = 1

"""

if __name__ == "__main__":
    # print(run_query(query_1))
    # print(run_query(query_2))
    # print(run_query(query_3))
    # print(run_query(query_4))
    # print(run_query(query_5))
    # print(run_query(query_6))
    # print(run_query(query_7))
    # print(run_query(query_8))
    # print(run_query(query_9))
    print(run_query(query_10))
