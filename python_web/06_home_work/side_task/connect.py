import psycopg2

# Define your connection details
def get_connection():
    return psycopg2.connect(
        dbname="hw6pi24",
        user="postgres",
        password="567234",
        host="195.201.150.230",  # For local, use 'localhost'
        port="5433"   # Default port for PostgreSQL is 5432
    )

# Manage the connection outside of the function
conn = get_connection()

def run_query(query: str, data: tuple | None = None) -> list[tuple]:
    # Create a cursor object
    cur = conn.cursor()

    print(query, data)
    # Execute the query
    if data:
        cur.execute(query, data)
    else:
        cur.execute(query)

    # Check if it’s a SELECT query to fetch results
    if query.strip().lower().startswith("select"):
        rows = cur.fetchall()  # Fetch all rows
    else:
        # If it's an INSERT/UPDATE/DELETE query, commit the changes
        conn.commit()
        rows = []  # No rows to fetch for non-SELECT queries

    # Close the cursor
    cur.close()

    # Return fetched rows (for SELECT queries)
    return rows

# Function to close the connection when done
def close_connection():
    conn.close()
