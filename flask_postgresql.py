import os
import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="fish_db",
        user=os.environ['Fish_admin '],
        password=os.environ['admin12345'])

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS fishes;')
cur.execute('CREATE TABLE fishes (id serial PRIMARY KEY,'
                                 'Color varchar (2000) NOT NULL,'
                                 'Skin_Type varchar (100) NOT NULL,'
                                 'Lifespan varchar (100) NOT NULL,'
                                 'Weight varchar (100) NOT NULL', 
                                 'Age_of_Sexual_Maturity varchar (100) NOT NULL', 
                                 'Length integer NOT NULL,'
                                 'review text,'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )

# Insert data into the table

cur.execute('INSERT INTO books (title, author, pages_num, review)'
            'VALUES (%s, %s, %s, %s)',
            ('A Tale of Two Cities',
             'Charles Dickens',
             489,
             'A great classic!')
            )


cur.execute('INSERT INTO books (title, author, pages_num, review)'
            'VALUES (%s, %s, %s, %s)',
            ('Anna Karenina',
             'Leo Tolstoy',
             864,
             'Another great classic!')
            )

conn.commit()

cur.close()
conn.close()