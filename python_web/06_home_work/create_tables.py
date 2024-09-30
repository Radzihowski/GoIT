from connect import run_query

student_table='''
    CREATE TABLE IF NOT EXISTS students (
     id SERIAL PRIMARY KEY,
     first_name text NOT NULL,
     second_name text NOT NULL
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
     teacher_id integer NOT NULL,
     title text NOT NULL,
     FOREIGN KEY (teacher_id) REFERENCES teachers (id)
    );
'''


if __name__ == "__main__":
    run_query(student_table)
    run_query(groups)
    run_query(teachers)
    run_query(subjects)
