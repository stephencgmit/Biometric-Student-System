#!/usr/bin/env python3

import sqlite3

def create():
    try:
        c.execute("""CREATE TABLE students
                 (templateid, firstname, lastname, q1, q2, q3)""")
    except:
        pass
    
def insert():
    templateid = 1
    firstname = "Stephen"
    lastname = "Coyne"
    #params(templateid, firstname, lastname)
    c.execute("INSERT INTO students VALUES ('1', 'Stephen', 'LeftThumb', 'NULL','NULL','NULL')")

conn = sqlite3.connect('student.db')
c = conn.cursor()

#create()
insert()
conn.commit()

c.close()

# CREATING THE DATABASE ############################
# c.execute("""CREATE TABLE students (
#             templateID int,
#             firstname text,
#             fullname text,
#             q1 int,
#             q2 int,
#             q3 int
#             )""") # DOC STRING. DONE THIS WAY IN PYTHON DOCUMENTATION
