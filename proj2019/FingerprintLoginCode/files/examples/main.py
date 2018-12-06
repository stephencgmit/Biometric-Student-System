#!/usr/bin/env python3

import sqlite3
from pyfingerprint.pyfingerprint import PyFingerprint
import datetime
import tempfile
import hashlib
import Quiz1, Quiz2, Quiz3, example_search_wait, example_enroll_wait
import time
from tkinter import *
from tkinter import messagebox

conn = sqlite3.connect('student.db')
c = conn.cursor()

global returned_score
#global idnum
#idnum = 0
returned_score = 0
################## CREATING THE DATABASE ############################
# c.execute("""CREATE TABLE students (
#             fullname text,
#             password text
#             )""") # DOC STRING. DONE THIS WAY IN PYTHON DOCUMENTATION


################# ADDING USERS TO DATABASE #######################
#c.execute("INSERT INTO students VALUES ('Stephen Coyne', '123')")

def main():
    conn.commit()
    main_menu()
    conn.commit()
    conn.close()


def main_menu():
    register_login_query = input("Choose\n1. Login\n2. Register\n3. Query Database\n4. Add Table to Database\n5."
                                 " Download Fingerprint Image\n")
    if register_login_query == '1':
        login()
    elif register_login_query == '2':
        register()
    elif register_login_query == '3':
        choose_query()
    elif register_login_query == '4':
        add_database_table()
    elif register_login_query == '5':
        download_fingerprint_image()
    else:
        print("Input error. Select again")
        main_menu()


def choose_query():
    admin_access = input("Enter admin password for access to database: ")
    if admin_access == '12345':
        query = input("Hi admin! Choose Query type: \n1. Show Students\n2. Delete Student\n")
        if query == '1':
            c.execute("SELECT templateid, firstname, lastname, q1, q2, q3 FROM students")
            list_users = c.fetchall()
            for x in list_users:
                print(x)
            main()
        elif query == '2':
            #temp = input("Choose name to delete: ")
            #c = conn.cursor()
            c.execute("DELETE from students where templateid = 7 ")
            print(c.rowcount, "record(s) deleted")
            conn.commit()
            main()
    else:
        print("Wrong password")
        main()


def register():
    example_enroll_wait.run()
    #from example_enroll_wait import idnum
    #print("value passed from example_enroll_wait is %d", idnum)
    #time.sleep(1)
    #with open("/home/pi/Desktop/ProjectCode/pyfingerprint/src/files/examples/idtemplate.txt", "r") as f:
    #    print(f)
    #    f.close()
    #firstname = input("Enter your name: ")
    #lastname = input("Enter your password: ")
    #c.execute("INSERT INTO students VALUES(?, ?, ?, ?, ?, ?);", (idnum, firstname, lastname, 'NULL', 'NULL', 'NULL'))
    #conn.commit()
    main()


def login():
    #first = input("Enter fullname: ")
    #last = input("Enter password: ")
#print(c.fetchone())

### HOW TO QUERY and FIND USERS in database ###
# https://stackoverflow.com/questions/30041983/check-if-a-row-exists-in-sqlite3?noredirect=1&lq=1
    #for row in c.execute("SELECT * FROM students WHERE firstname = ? and lastname = ? ", (first, last, )):
        #n1, pw1 = row
    try:
        f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

        if ( f.verifyPassword() == False ):
            raise ValueError('The given fingerprint sensor password is wrong!')

    except Exception as e:
        print('The fingerprint sensor could not be initialized!')
        print('Exception message: ' + str(e))
        exit(1)

    ## Gets some sensor information
    print('Currently used templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))

    ## Tries to search the finger and calculate hash
    try:
        msg=messagebox.showinfo("Fingerprint Login", "Press OK when Finger Ready")

        #print('Waiting for finger...')

        ## Wait that finger is read
        while ( f.readImage() == False ):
            pass

        ## Converts read image to characteristics and stores it in charbuffer 1
        f.convertImage(0x01)

        ## Searchs template
        result = f.searchTemplate()

        positionNumber = result[0]
        accuracyScore = result[1]
        temp = positionNumber
        if ( positionNumber == -1 ):
            print('No match found! Try again')
            login()
        else:
            print('Found template at position #' + str(positionNumber))
            print('The accuracy score is: ' + str(accuracyScore))
            
            #for row in c:
            #    print(row)
            #print(c)
            print("User logged in")

        ## OPTIONAL stuff
        ##

        ## Loads the found template to charbuffer 1
        f.loadTemplate(positionNumber, 0x01)

        ## Downloads the characteristics of template loaded in charbuffer 1
        ##characterics = str(f.downloadCharacteristics(0x01)).encode('utf-8')

        ## Hashes characteristics of template
        ##print('SHA-2 hash of template: ' + hashlib.sha256(characterics).hexdigest())

    except Exception as e:
        print('Operation failed!')
        print('Exception message: ' + str(e))
        exit(1)
    
    
    # https://stackoverflow.com/questions/11853167/parameter-unsupported-when-inserting-int-in-sqlite/21082534
    c.execute("SELECT firstname, lastname from students WHERE templateid = ?", (temp,)) 
    print(c.fetchone())
    #''.join(
    #name = str(c.fetchone()[0])
    #print(name)

    choose_quiz = input("Choose Quiz: \n1. Electronic Principles\n"
                       "2. Electronic Principles 2\n3. Electronic Principles 3\n")
    if choose_quiz == '1':
        Quiz1.run_quiz1()
        from Quiz1 import percentage
        print("Score passed from Quiz 1 is: ", percentage)
        #c.execute("SELECT * FROM students WHERE fullname = ? and password = ? ", (user_name, user_pw,))
        c.execute("UPDATE students set q1 = ? WHERE templateid = ?", (percentage, positionNumber))
        main_menu()
        #break
    elif choose_quiz == '2':
        Quiz2.run_quiz2()
        from Quiz2 import percentage
        print("Score passed from Quiz 2 is: ", percentage)
        c.execute("UPDATE students set q2 = ? WHERE templateid = ?", (percentage, positionNumber))
        main_menu()
        #break
    elif choose_quiz == '3':
        Quiz3.run_quiz3()
        from Quiz3 import percentage
        print("Score passed from Quiz 3 is: ", percentage)
        c.execute("UPDATE students set q3 = ? WHERE templateid = ?", (percentage, positionNumber))
        main_menu()
        #break
    else:
        print("User not found in database: Try again\n")
        main()
        
        
def download_fingerprint_image():
    ## Tries to initialize the sensor
    try:
        f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

        if ( f.verifyPassword() == False ):
            raise ValueError('The given fingerprint sensor password is wrong!')

    except Exception as e:
        print('The fingerprint sensor could not be initialized!')
        print('Exception message: ' + str(e))
        exit(1)

    ## Gets some sensor information
    print('Currently used templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))

    ## Tries to read image and download it
    try:
        msg=messagebox.showinfo("Download Image", "Press OK when Finger Ready")

        ## Wait that finger is read
        while ( f.readImage() == False ):
            pass

        print('Downloading image (this take a while)...')

        imageDestination =  tempfile.gettempdir() + '/fingerprint.bmp'
        f.downloadImage(imageDestination)

        print('The image was saved to "' + imageDestination + '".')

    except Exception as e:
        print('Operation failed!')
        print('Exception message: ' + str(e))
        exit(1)


def add_database_table():
    #c.execute("ALTER TABLE students ADD COLUMN quiz3score int")
    main_menu()
    
#def delete_row():


if __name__ == "__main__":
    main()

