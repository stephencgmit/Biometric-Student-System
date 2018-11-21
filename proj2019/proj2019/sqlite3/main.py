import sqlite3
import Quiz1, Quiz2, Quiz3

conn = sqlite3.connect('student.db')
c = conn.cursor()
global returned_score
returned_score = 0
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
def main():
    main_menu()
    conn.commit()
    conn.close()


def main_menu():
    register_login_query = raw_input("Choose\n1. Login\n2. Register\n3. Query Database\n4. Add Table to Database\n")
    if register_login_query == '1':
        login()
    elif register_login_query == '2':
        register()
    elif register_login_query == '3':
        choose_query()
    elif register_login_query == '4':
        add_database_table()
    else:
        print("Input error. Select again")
        main_menu()


def choose_query():
    admin_access = raw_input("Enter admin password for access to database: ")
    if admin_access == '12345':
        query = raw_input("Hi admin! Choose Query type: \n1. Show Students\n2. Delete Student\n")
        if query == '1':
            c.execute("SELECT fullname, password, quiz1score, quiz2score, quiz3score FROM students")
            list_users = c.fetchall()
            for x in list_users:
                print(x)
            main()
        elif query == '2':
            f_name = raw_input("Choose name to delete: ")
            #c = conn.cursor()
            c.execute("DELETE from students where fullname = ? ", f_name)
            print(c.rowcount, "record(s) deleted")
            conn.commit()
            main()
    else:
        main()


def register():
    fullname = raw_input("Enter your name: ")
    password = raw_input("Enter your password: ")
    c.execute("INSERT INTO students VALUES(?, ?);", (fullname, password))
    conn.commit()
    main()


def login():
    user_name = raw_input("Enter fullname: ")
    user_pw = raw_input("Enter password: ")
#print(c.fetchone())

### HOW TO QUERY and FIND USERS in database ###
# https://stackoverflow.com/questions/30041983/check-if-a-row-exists-in-sqlite3?noredirect=1&lq=1
    for row in c.execute("SELECT * FROM students WHERE fullname = ? and password = ? ", (user_name, user_pw, )):
        #n1, pw1 = row
        print(row)
        print("User logged in")
        choose_quiz = raw_input("Choose Quiz: \n1. Electronic Principles\n"
                           "2.Electronic Principles 2\n3. Electronic Principles 3\n")
        if choose_quiz == '1':
            Quiz1.run_quiz1()
            from Quiz1 import score
            print("Score passed from Quiz 1 is : %d", score)
            #c.execute("SELECT * FROM students WHERE fullname = ? and password = ? ", (user_name, user_pw,))
            c.execute("UPDATE students set quiz1score = ? WHERE fullname = ? and "
                      "password = ? ", (score, user_name, user_pw))
            break
        elif choose_quiz == '2':
            Quiz2.run_quiz2()
            from Quiz2 import score
            print("Score passed from Quiz 2 is %d: ", score)
            c.execute("UPDATE students set quiz2score = ? WHERE fullname = ? and "
                      "password = ? ", (score, user_name, user_pw))

            break
        elif choose_quiz == '3':
            Quiz3.run_quiz3()
            from Quiz3 import score
            print("Score passed from Quiz 3 is %d: ", score)
            c.execute("UPDATE students set quiz3score = ? WHERE fullname = ? and "
                      "password = ? ", (score, user_name, user_pw))
            break
    else:
        print("User not found in database: Try again\n")
        main()


def add_database_table():
    #c.execute("ALTER TABLE students ADD COLUMN quiz3score int")
    main_menu()


if __name__ == "__main__":
    main()
