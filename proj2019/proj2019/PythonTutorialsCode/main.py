from random import shuffle
import time
global score
score = 0


def run_quiz2():
    print("***** Welcome to quiz 2 *****")
    question1()
    question2()
    question3()
    time.sleep(0.1)
    print("Your final score is: ")
    print(score)


def question1():
    q1 = raw_input("Q1. What's the resistance of 2 resistors in parallel with values of 200 and 100?\n"
                   "Choose:  A) 66.667. 	B) 150 	    C) 125\n")
    if q1 == "A" or q1 == "a":
        print("Correct!")
        score += 1
    elif q1 == "B" or q1 == "b" or q1 == "C" or q1 == "c":
        print("Incorrect!")
    else:
        print("Not a valid answer. Try again")
        question1()


def question2():
    q2 = raw_input("Q2. What's the voltage across a 220 ohm resistor when a current of 3mA flows through?\n"
                   "Choose:  A) 6.6V. 	B) 0.66V 	C) 0.06V\n")
    if q2 == "B" or q2 == "b":
        print("Correct!")
        score += 1
    elif q2 == "A" or q2 == "a" or q2 == "C" or q2 == "c":
        print("Incorrect!")
    else:
        print("Not a valid answer. Try again")
        question2()


def question3():
    q3 = raw_input("Q3. The voltage across a 2.7k resistor is 5.4V. What current flows?\n"
                   "Choose:  A) 2mA. 	B) 20mA 	C) 200uA\n")
    if q3 == "A" or q3 == "a":
        print("Correct!")
        score += 1
    elif q3 == "B" or q3 == "b" or q3 == "C" or q3 == "c":
        print("Incorrect!")
    else:
        print("Not a valid answer. Try again")
        question2()


def question4():
    q4 = raw_input("Q4. How much electrical energy in joules does a 20W soldering iron change in 1 minute?\n"
                   "Choose:  A) 3J. 	B) 20J 	C) 1200J\n")
    if q4 == "C" or q4 == "c":
        print("Correct!")
        score += 1
    elif q4 == "A" or q4 == "a" or q4 == "B" or q4 == "b":
        print("Incorrect!")
    else:
        print("Not a valid answer. Try again")
        question4()


def question5():
    q5 = raw_input("Q5. A current of 2A passes through a resistance of 4ohm. Calc the voltage across & the power used\n"
                   "Choose:  A) 66.667. 	B) 150 	C) 8V and 16W\n")
    if q5 == "C" or q5 == "c":
        print("Correct!")
        score += 1
    elif q5 == "A" or q5 == "a" or q5 == "B" or q5 == "b":
        print("Incorrect!")
    else:
        print("Not a valid answer. Try again")
        question5()


def question6():
    q6 = raw_input("Q6. Lamp is labelled 12V 36W. What current will it take on 12V supply and what is its resistance?\n"
                   "Choose:  A) 3A and 4 ohms. 	B) 3A and 4 ohms 	C) 3A and 3 ohms\n")
    if q6 == "B" or q6 == "b":
        print("Correct!")
        score += 1
    elif q6 == "A" or q6 == "a" or q6 == "C" or q6 == "c":
        print("Incorrect!")
    else:
        print("Not a valid answer. Try again")
        question6()


def question7():
    q7 = raw_input("Q7. What is the printed code for the following resistor? 100 ohm and 5% tolerance\n"
                   "Choose:  A) Black Brown Brown Gold. 	B) Brown Black Red Gold 	C) Brown Black Brown Gold")
    if q7 == "C" or q7 == "c":
        print("Correct!")
        score += 1
    elif q7 == "A" or q7 == "a" or q7 == "B" or q7 == "b":
        print("Incorrect!")
    else:
        print("Not a valid answer. Try again")
        question7()


def question8():
    q8 = raw_input("Q8. What is the printed code for the following resistor? 4.7k ohm and 2% tolerance\n"
                   "Choose:  A) Orange Red Orange Red. 	B) Orange Violet Red Green 	C) Yellow Violet Red Red")
    if q8 == "C" or q8 == "c":
        print("Correct!")
        score += 1
    elif q8 == "A" or q8 == "a" or q8 == "B" or q8 == "b":
        print("Incorrect!")
    else:
        print("Not a valid answer. Try again")
        question8()


def main():
    lis = [question2, question1, question3, question4, question5, question6, question7, question8]         # LIST OF FUNCTIONS.
    shuffle(lis)                                    # RUN THE SHUFFLED FUNCTIONS

    for i in lis:
        i()


if __name__ == "__main__":
    main()
