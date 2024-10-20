from connect import run_query

cities_table = '''
    CREATE TABLE IF NOT EXISTS cities (
    id SERIAL PRIMARY KEY,
    name text NOT NULL,
    City text NOT NULL
    );
'''

if __name__ == '__main__':
    run_query(cities_table)