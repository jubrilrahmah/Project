import csv
import psycopg2
conn = psycopg2.connect("host=localhost dbname=demo_db user=postgres password=pass")

c = conn.cursor()
# c.execute(""" CREATE TABLE students_result (Name text, 
#                         Maths integer, 
#                         English integer,
#                         Pysics Integer,
#                         Biology integer)
# """)

conn.commit()

# loading my csvfile
with open('student_result.csv', 'r') as f:
    read = csv.reader(f) #csv module
    next(read) # Skip the header row.

    for row in read:
        c.execute("""INSERT INTO students_result VALUES (%s, %s, %s, %s, %s)""", row)

#Not this can be done the other way without using the for loop, 
#THis can be done using a postgress specific command




conn.commit()
conn.close()
