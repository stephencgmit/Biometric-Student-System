# calling a python script on button click using python and tkinter
# https://stackoverflow.com/questions/26852465/calling-a-python-script-on-button-click-using-python-and-tkinter

# Pass variable between python scripts
# https://stackoverflow.com/questions/16048237/pass-variable-between-python-scripts

# Function calls in a list.
# https://stackoverflow.com/questions/5465455/syntax-to-call-random-function-from-a-list

# https://stackoverflow.com/questions/48218505/shuffling-a-list-of-functions-with-random-shuffle

# https://stackoverflow.com/questions/39952782/how-to-run-functions-in-random-order

import time
from random import shuffle

global score
score = 0
#score = 0


def run_quiz1():
    print("***** Welcome to quiz 1 *****")
    #global score
    #score = 0
    lis = [question2, question1, question3, question4, question5, question6, question7, question8,
           question9, question10, question11, question12, question13, question14, question15,
           question16, question17, question18, question19, question20]         # LIST OF FUNCTIONS.
    shuffle(lis)                                    # RUN THE SHUFFLED FUNCTIONS

    for i in lis:
        i()
    time.sleep(0.1)
    print("Your final score is: ")
    print(score)


def question1():
    q1 = input("What's the resistance of 2 resistors in parallel with values of 200 and 100?\n"
                   "Choose:  A) 66.667.     B) 150      C) 125\n")
    if q1 == "A" or q1 == "a":
        print("Correct!")
        global score
        score += 1
    elif q1 == "B" or q1 == "b" or q1 == "C" or q1 == "c":
        print("Incorrect!")
    else:
        print("Not a valid answer. Try again")
        question1()


def question2():
    q2 = input("What's the voltage across a 220 ohm resistor when a current of 3mA flows through?\n"
                   "Choose:  A) 6.6V.   B) 0.66V    C) 0.06V\n")

    if q2 == "B" or q2 == "b":
        print("Correct!")
        global score
        score += 1
    elif q2 == "A" or q2 == "a" or q2 == "C" or q2 == "c":
        print("Incorrect!")
    else:
        print("Not a valid answer. Try again")
        question2()


def question3():
    q3 = input("The voltage across a 2.7k resistor is 5.4V. What current flows?\n"
                   "Choose:  A) 2mA.    B) 20mA     C) 200uA\n")
    if q3 == "A" or q3 == "a":
        print("Correct!")
        global score
        score += 1
    elif q3 == "B" or q3 == "b" or q3 == "C" or q3 == "c":
        print("Incorrect!")
    else:
        print("Not a valid answer. Try again")
        question2()


def question4():
    q4 = input("How much electrical energy in joules does a 20W soldering iron change in 1 minute?\n"
                   "Choose:  A) 3J.     B) 20J  C) 1200J\n")
    if q4 == "C" or q4 == "c":
        print("Correct!")
        global score
        score += 1
    elif q4 == "A" or q4 == "a" or q4 == "B" or q4 == "b":
        print("Incorrect!")
    else:
        print("Not a valid answer. Try again")
        question4()


def question5():
    q5 = input(
        "A current of 2A passes through a resistance of 4ohm. Calculate the voltage across and the power used\n"
        "Choose:  A) 66.667.    B) 150  C) 8V and 16W\n")
    if q5 == "C" or q5 == "c":
        print("Correct!")
        global score
        score += 1
    elif q5 == "A" or q5 == "a" or q5 == "B" or q5 == "b":
        print("Incorrect!")
    else:
        print("Not a valid answer. Try again")
        question5()


def question6():
    q6 = input("Lamp is labelled 12V 36W. What current will it take on 12V supply and what is its resistance?\n"
                   "Choose:  A) 3A and 4 ohms.  B) 3A and 4 ohms    C) 3A and 3 ohms\n")
    if q6 == "B" or q6 == "b":
        print("Correct!")
        global score
        score += 1
    elif q6 == "A" or q6 == "a" or q6 == "C" or q6 == "c":
        print("Incorrect!")
    else:
        print("Not a valid answer. Try again")
        question6()


def question7():
    q7 = input("What is the printed code for the following resistor? 100 ohm and 5% tolerance\n"
                   "Choose:  A) Black Brown Brown Gold.     B) Brown Black Red Gold     C) Brown Black Brown Gold")
    if q7 == "C" or q7 == "c":
        print("Correct!")
        global score
        score += 1
    elif q7 == "A" or q7 == "a" or q7 == "B" or q7 == "b":
        print("Incorrect!")
    else:
        print("Not a valid answer. Try again")
        question7()


def question8():
    q8 = input("What is the printed code for the following resistor? 4.7k ohm and 2% tolerance\n"
                   "Choose:  A) Orange Red Orange Red.  B) Orange Violet Red Green  C) Yellow Violet Red Red")
    if q8 == "C" or q8 == "c":
        print("Correct!")
        global score
        score += 1
    elif q8 == "A" or q8 == "a" or q8 == "B" or q8 == "b":
        print("Incorrect!")
    else:
        print("Not a valid answer. Try again")
        question8()


def question9():
    q9 = input("What is the printed code for the following resistor? 18k ohm and 1% tolerance\n"
                   "Choose:  A) Gray Brown Orange Blue  B) Brown Gray Orange Brown  C) Brown Yellow Red Brown\n")
    if q9 == "A" or q9 == "a":
        print("Correct!")
        global score
        score += 1
    elif q9 == "B" or q9 == "b" or q9 == "C" or q9 == "c":
        print("Incorrect!")
    else:
        print("Not a valid answer. Try again")
        question9()


def question10():
    q10 = input("What is the printed code for the following resistor? 390k ohm and 20% tolerance\n"
                    "Choose:  A) Orange White Yellow Gold.  B) Red White Orange Gold    C) Orange Blue Yellow Brown\n")
    if q10 == "A" or q10 == "a":
        print("Correct!")
        global score
        score += 1
    elif q10 == "B" or q10 == "b" or q10 == "C" or q10 == "c":
        print("Incorrect!")
    else:
        print("Not a valid answer. Try again")
        question10()


def question11():
    q11 = input("What's the electrical power dissipated in a 100 ohm resistor carrying a current of 50mA?\n"
                    "Choose:  A) .25W.  B) 5W   C) 2.5W\n")
    if q11 == "A" or q11 == "a":
        print("Correct!")
        global score
        score += 1
    elif q11 == "B" or q11 == "b" or q11 == "C" or q11 == "c":
        print("Incorrect!")
    else:
        print("Not a valid answer. Try again")
        question11()


def question12():
    q12 = input("What's the wattage of a 6V 60mA lamp?\n"
                    "Choose:  A) 3.6W.  B) 10W  C) .36W\n")
    if q12 == "C" or q12 == "c":
        print("Correct!")
        global score
        score += 1
    elif q12 == "B" or q12 == "b" or q12 == "A" or q12 == "a":
        print("Incorrect!")
    else:
        print("Not a valid answer. Try again")
        question12()


def question13():
    q13 = input("What is the charge stored when the voltage across a 100000 uF capacitor is 10V?\n"
                    "Choose:  A) 1 Coulomb.     B) .1 Coulomb   C) 10 Coulombs\n")
    if q13 == "A" or q13 == "a":
        print("Correct!")
        global score
        score += 1
    elif q13 == "B" or q13 == "b" or q13 == "C" or q13 == "c":
        print("Incorrect!")
    else:
        print("Not a valid answer. Try again")
        question13()


def question14():
    q14 = input("What's the charge stored when the voltage across a 50 uF capacitor is 9V?\n"
                    "Choose:  A) 45 uC.     B) 450 uC   C) 4500 uC\n")
    if q14 == "B" or q14 == "b":
        print("Correct!")
        global score
        score += 1
    elif q14 == "A" or q14 == "a" or q14 == "C" or q14 == "c":
        print("Incorrect!")
    else:
        print("Not a valid answer. Try again")
        question14()


def question15():
    q15 = input("Calculate the energy stored in a capacitor with a charge of 2C and 9V across its plates?\n"
                    "Choose:  A) 18J.   B) 4.5J     C) 9J\n")
    if q15 == "C" or q15 == "c":
        print("Correct!")
        global score
        score += 1
    elif q15 == "A" or q15 == "a" or q15 == "B" or q15 == "b":
        print("Incorrect!")
    else:
        print("Not a valid answer. Try again")
        question15()


def question16():
    q16 = input("Calculate the energy stored in a 1uF capacitor charged to 500V\n"
                    "Choose:  A) 12.5J  B) 1.25J    C) .125J\n")
    if q16 == "C" or q16 == "c":
        print("Correct!")
        global score
        score += 1
    elif q16 == "A" or q16 == "a" or q16 == "B" or q16 == "b":
        print("Incorrect!")
    else:
        print("Not a valid answer. Try again")
        question16()


def question17():
    q17 = input("Calculate the reactance of a 1uF capacitor at frequencies of 1KHz?\n"
                    "Choose:  A) 109 ohms.  B) 159 ohms     C) 189 ohms\n")
    if q17 == "B" or q17 == "b":
        print("Correct!")
        global score
        score += 1
    elif q17 == "A" or q17 == "a" or q17 == "C" or q17 == "c":
        print("Incorrect!")
    else:
        print("Not a valid answer. Try again")
        question17()


def question18():
    q18 = input("What's the combined capacitance of a 2.2uF and 4.7uF in parallel?\n"
                    "Choose:  A) 6.9uF.     B) 1.5uF    C) 3.45uF\n")
    if q18 == "A" or q18 == "a":
        print("Correct!")
        global score
        score += 1
    elif q18 == "C" or q18 == "c" or q18 == "B" or q18 == "b":
        print("Incorrect!")
    else:
        print("Not a valid answer. Try again")
        question18()


def question19():
    q19 = input("What's the combined capacitance of two 100uF capacitors in series?\n"
                    "Choose:  A) 200uF.     B) 100uF    C) 50uF\n")
    if q19 == "C" or q19 == "c":
        print("Correct!")
        global score
        score += 1
    elif q19 == "A" or q19 == "a" or q19 == "B" or q19 == "b":
        print("Incorrect!")
    else:
        print("Not a valid answer. Try again")
        question19()


def question20():
    q20 = input("What value of capacitance would give a reactance of 50 ohm at 700Hz?\n"
                    "Choose:  A) 455uF.     B) 4.55uF   C) 45.5uF\n")
    if q20 == "B" or q20 == "b":
        print("Correct!")
        global score
        score += 1
    elif q20 == "A" or q20 == "a" or q20 == "C" or q20 == "c":
        print("Incorrect!")
    else:
        print("Not a valid answer. Try again")
        question20()


#run_quiz2()
