from connect import run_query

query =  """  
    SELECT c.city, COUNT(*) as city 
    FROM cities c
    GROUP BY c.city
    LIMIT 5;
"""

if __name__ == "__main__":
    print(run_query(query))