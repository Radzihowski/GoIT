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
     group_name text NOT NULL,
    );
'''


if __name__ == "__main__":
    run_query(student_table)
