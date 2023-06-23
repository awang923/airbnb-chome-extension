import psycopg2

conn = psycopg2.connect(host='localhost', dbname='postgres', user='postgres',
                        password='Admin123', port=5433)

cur = conn.cursor()

create_table = """
    CREATE TABLE IF NOT EXISTS listings (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        price NUMERIC(10, 2),
        reviews INTEGER
    );
"""


cur.execute(create_table)

conn.commit()

cur.close()
conn.close()