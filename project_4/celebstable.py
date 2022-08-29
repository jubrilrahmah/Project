from distutils.util import execute
import sqlite3
from tkinter import Y



#connect or create to a database "i.e student databse= student.db"
conn = sqlite3.connect("celebrity.db")
#check that the connection is succesful
print("Database created successfully", type(conn))

#create a cusor object that allows the execution of SQL statement
cursor = conn.cursor()

#verify that the cusor is created successfully
print("cursosr created successfully", type(cursor))

#creating the table celebs 
# celebs = """
#         CREATE TABLE celebrity (
#                 names text, age integer, years_in_industry integer, num_albums integer, genre text, awards integer)
#         """

# cursor.execute(celebs)
# celebs = [("Justin Mark", 30, 8, 5, "Rnb", 10), ("Mario John", 28, 7, 2, "Ragge" , 12),
#             ("Ruth Wash", 45, 20, 6, "Ragge" ,30),  ("Eric Lana", 25, 4, 2, "Hip-hop", 5),
#             ("Ayinla Akintola", 56, 21, 15, "Apala", 25), ("Ted Alli", 50, 21, 10, "Fuji", 20),
#             ("Reina Fransis", 21, 3, 1, "Hip-hop", 1), ("Omojola Aayi", 45, 17, 7, "Fuji", 17),
#             ("Allyson Show", 26, 7, 5, "Hip-hop", 16), ("Dekunle Philip", 30, 8, 4, "Hip-hop", 18),
#             ("Lara Jackson", 56, 16, 20, "Ragge", 22), ("Teee John", 26, 5, 1, "Hip-hop", 4),
#             ("Destiny Mark", 52, 23, 12, "Ragge", 17), ("Phyne Dickson", 30, 7, 4, "Rnb", 6),
#             ("Ajayi Sowole", 70, 35, 13, "Apala", 29), ("Gideaon Joe", 20, 2, 1, "Hip-hop", 3),
#             ("Bella Smith", 19, 3, 1, "Hip-hop", 2), ("Donald Cole", 27, 7, 3, "Hip-hop", 8),
#             ("Ella Smart", 19, 1, 1, "Hip-hop", 0), ("Joseph Mole", 26, 6, 2, "Hip-hop", 3)
#             ]


# cursor.executemany("INSERT INTO celebrity VALUES (?, ?, ?, ?, ?, ?)", (celebs))

print("\nTable excecuted successfully")

print("Recorded value: ", cursor.rowcount)

conn.commit()

conn.close()