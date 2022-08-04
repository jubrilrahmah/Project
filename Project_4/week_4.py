# from curses import ACS_GEQUAL
from distutils.util import execute
import sqlite3

from colorama import Cursor

#connect or create to a database "i.e student databse= student.db"
conn = sqlite3.connect("student.db")
#check that the connection is succesful
print("Database created successfully", type(conn))

#create a cusor object that allows the execution of SQL statement
cursor = conn.cursor()

#verify that the cusor is created successfully
print("cursosr created successfully", type(cursor))

print("\nWeek4 Project")

# Create a dummy celebrity dataset with the following features name, genre, num_albums, age, awards, years_in_industry
# Create a celebs database in sqlite and insert the dataset into it
# Make your celebrity dataset have at least 20 rows (i.e 20 unique records)
# Query your data to answer the following questions:
#  - Who is the most decorated celebrity?
#  - Who is the oldest celebrity?
#  - Which celebrity has been in the industry the longest?
#  - Which celebrity has the least number of albums?
#  - What is the most popular genre of music amongst all celebrities in the dataset?
# Research on python f strings

celebr = """
        CREATE TABLE IF NOT EXISTS celebr (
                name text, age integer, years_in_industry integer, num_albums integer, genre text, awards integer)
        """
cursor.execute(celebr)

#Inserting values into table

celebr = [("Justin Mark", 30, 8, 5, "Rnb", 10), ("Mario John", 28, 7, 2, "Ragge" , 12),
            ("Ruth Wash", 45, 20, 6, "Ragge" ,30),  ("Eric Lana", 25, 4, 2, "Hip-hop", 5),
            ("Ayinla Akintola", 56, 21, 15, "Apala", 25), ("Ted Alli", 50, 21, 10, "Fuji", 20),
            ("Reina Fransis", 21, 3, 1, "Hip-hop", 1), ("Omojola Aayi", 45, 17, 7, "Fuji", 17),
            ("Allyson Show", 26, 7, 5, "Hip-hop", 16), ("Dekunle Philip", 30, 8, 4, "Hip-hop", 18),
            ("Lara Jackson", 56, 16, 20, "Ragge", 22), ("Teee John", 26, 5, 1, "Hip-hop", 4),
            ("Destiny Mark", 52, 23, 12, "Ragge", 17), ("Phyne Dickson", 30, 7, 4, "Rnb", 6),
            ("Ajayi Sowole", 70, 35, 13, "Apala", 29), ("Gideaon Joe", 20, 2, 1, "Hip-hop", 3),
            ("Bella Smith", 19, 3, 1, "Hip-hop", 2), ("Donald Cole", 27, 7, 3, "hip-hop", 8),
            ("Ella Smart", 19, 0, 1, "Hip-hop", 0), ("Joseph Mole", 26, 6, 2, "hip-hop", 3)
            ]

cursor.executemany("INSERT INTO celebr VALUES (?, ?, ?, ?, ?, ?)", (celebr))

print("\nTable excecuted successfully")

print("Recorded value: ", cursor.rowcount)

for i in celebr:
         name, age, years_in_industry, num_albums, genre, awards = i
         print(f" \n {name} \t\t  {age} \t\t {years_in_industry} \t\t {num_albums} \t\t  {genre}, \t\t {awards}")

#answering the queries
def queries(column1, column2):
        q = f"""
                SELECT {column1}
                FROM celebr
                ORDER BY {column2} DESC """

        cursor.execute(q)
        item = cursor.fetchmany(1)
        print(item)


print("\n Most decorated celeberity")
queries("name","awards") 

print("\n Oldest celebrity")
queries("name", "age") 

print("\n Celebrity that has been in the insdustry for long")
queries("name", "years_in_industry")

def querie(column_m, column_q):
        que = f"""
        SELECT {column_m}
        FROM celebr
        ORDER BY {column_q}   """
                
        cursor.execute(que)
        item = cursor.fetchmany(1)
        print(item)


print("\n celebrity with least no of album")
querie("name", "num_albums")

#find the the most popular genre
def quer(column1):
        qu = f"""
         SELECT {column1}
         FROM celebr
         ORDER BY {column1} DESC """
         
        cursor.execute(qu)
        item = cursor.fetchmany(1)
        print(item)

print("\n The most popular genre")
quer("genre")

#commmit the database and the table
conn.commit()

#close the connection to the database
conn.close()
