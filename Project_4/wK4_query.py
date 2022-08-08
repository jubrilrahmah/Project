# from curses import ACS_GEQUAL
from distutils.util import execute
import sqlite3

from colorama import Cursor

#connect or create to a database "i.e student databse= student.db"
conn = sqlite3.connect("celebrity.db")
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
print("."*50)
print("Week4 project")
print("queries on celebs table")

p = """SELECT *
        FROM celebs"""

q = cursor.execute(p)     
for i in q:
         names, age, years_in_industry, num_albums, genre, awards = i
         print(f" \n {names} \t\t  {age} \t\t {years_in_industry} \t{num_albums} \t{genre}, \t {awards}")
         #The (\t) is use to give space between output while printing 



def queries(column1, column2):
         q = f"""
                SELECT {column1}
               FROM celebs
                 ORDER BY {column2} DESC; """

         cursor.execute(q)
         item = cursor.fetchmany(1)
         print(item)


print("\n Most decorated celeberity")
queries("names","awards") #Most decorated

print("\n Oldest celebrity")
queries("names", "age") #oldes celebrity

print("\n Celebrity that has been in the insdustry for long")
queries("names", "years_in_industry")

def querie(column_m, column_q):
         que = f"""
         SELECT {column_m}
         FROM celebs
         ORDER BY {column_q}   """
                
         cursor.execute(que)
         item = cursor.fetchmany(1)
         print(item)


print("\n celebrity with least no of album")
querie("names", "num_albums")

#find the the most popular genre
# def quer(column1):
qu = """
         SELECT   genre, count(genre) AS cou
         FROM celebs
         GROUP BY genre
         ORDER BY cou  DESC
         LIMIT (1) ;"""

y= cursor.execute(qu)
z= cursor.fetchall()
print("\n The most popular genre is : ", z)

# commmit the database and the table
conn.commit()

#close the connection to the database
conn.close()
