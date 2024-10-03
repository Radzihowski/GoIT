from connect import run_query

student_table='''
    CREATE TABLE IF NOT EXISTS students (
     id SERIAL PRIMARY KEY,
     first_name text NOT NULL,
     second_name text NOT NULL,
     group_id INTEGER NOT NULL,
     FOREIGN KEY (group_id) REFERENCES groups (id)
    );
'''

groups='''
    CREATE TABLE IF NOT EXISTS groups (
     id SERIAL PRIMARY KEY,
     group_name text NOT NULL
    );
'''

teachers='''
    CREATE TABLE IF NOT EXISTS teachers (
     id SERIAL PRIMARY KEY,
     title text NOT NULL,
     first_name text NOT NULL,
     second_name text NOT NULL
    );
'''

subjects='''
    CREATE TABLE IF NOT EXISTS subjects (
     id SERIAL PRIMARY KEY,
     teacher_id INTEGER NOT NULL,
     title text NOT NULL,
     FOREIGN KEY (teacher_id) REFERENCES teachers (id)
    );
'''

marks='''
    CREATE TABLE IF NOT EXISTS marks (
     id SERIAL PRIMARY KEY,
     mark INTEGER NOT NULL,
     student_id INTEGER NOT NULL,
     subject_id INTEGER NOT NULL,
     date DATE NOT NULL,
     FOREIGN KEY (student_id) REFERENCES students (id),
     FOREIGN KEY (subject_id) REFERENCES subjects (id)
    );
'''


if __name__ == "__main__":
    run_query(groups)
    run_query(student_table)
    run_query(teachers)
    run_query(subjects)
    run_query(marks)
