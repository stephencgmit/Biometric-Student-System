import sqlite3

conn = sqlite3.connect('student.db')

c = conn.cursor()

################## CREATING THE DATABASE ############################
# c.execute("""CREATE TABLE students (
#             fullname text,
#             password text
#             )""") # DOC STRING. DONE THIS WAY IN PYTHON DOCUMENTATION


################# ADDING USERS TO DATABASE #######################
#c.execute("INSERT INTO students VALUES ('Stephen Coyne', '123')")
# c.execute("INSERT INTO students VALUES ('PERSON2', 'ABC')")
# c.execute("INSERT INTO students VALUES ('PERSON3', '456')")
# c.execute("INSERT INTO students VALUES ('PERSON4', 'QWERTY')")
# c.execute("INSERT INTO students VALUES ('PERSON5', 'HORSE')")
# c.execute("INSERT INTO students VALUES ('PERSON6', 'DOG')")
# c.execute("INSERT INTO students VALUES ('PERSON7', 'RED')")
# c.execute("INSERT INTO students VALUES ('PERSON8', 'IRELAND')")
# c.execute("INSERT INTO students VALUES ('PERSON9', 'BLUE')")
# c.execute("INSERT INTO students VALUES ('PERSON10', 'TOYOTA')")
# c.execute("INSERT INTO students VALUES ('PERSON11', 'GIANT')")

fName = raw_input("Enter fullname: ")

password = raw_input("Enter password: ")

#print(c.fetchone())

######################## HOW TO QUERY and FIND USERS in database #######################
# https://stackoverflow.com/questions/30041983/check-if-a-row-exists-in-sqlite3?noredirect=1&lq=1
for row in c.execute("SELECT * FROM students WHERE fullname = ? and password = ? ", (fName, password, )):
    n1, pw1 = row
    print("user logged in")
    break
else:
    print("user not found")

conn.commit()
conn.close()
