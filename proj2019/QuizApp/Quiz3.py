# calling a python script on button click using python and tkinter
# https://stackoverflow.com/questions/26852465/calling-a-python-script-on-button-click-using-python-and-tkinter
# Pass variable between python scripts
# https://stackoverflow.com/questions/16048237/pass-variable-between-python-scripts

import time

print("***** Welcome to quiz 3 *****")

score = 0
q1 = raw_input("What's the resistance of 2 resistors in parallel with values of 200 and 100?\n"
               "Choose:  A) 66.667. 	B) 150 	    C) 125\n")
if q1 == "A" or q1 == "a":
    print("Correct!")
    score += 1
else:
    print("incorrect!")

q2 = raw_input("What's the voltage across a 470 ohm resistor when a current of 3mA flows through?\n"
               "Choose:  A) 6.6V. 	B) 0.66V 	C) 0.06V\n")
if q2 == "B" or q2 == "b":
    print("Correct!")
    score += 1
else:
    print("incorrect!")

q3 = raw_input("The voltage across a 2.7k resistor is 5.4V. What current flows?\n"
               "Choose:  A) 2mA. 	B) 20mA 	C) 200uA\n")
if q3 == "A" or q3 == "a":
    print("Correct!")
    score += 1
else:
    print("incorrect!")

q4 = raw_input("How much electrical energy in joules does a 20W soldering iron change in 1 minute?\n"
               "Choose:  A) 3J. 	B) 20J 	C) 1200J\n")
if q4 == "C" or q4 == "c":
    print("Correct!")
    score += 1
else:
    print("incorrect!")

q5 = raw_input("A current of 2A passes through a resistance of 4ohm. Calculate the voltage across and the power used\n"
               "Choose:  A) 66.667. 	B) 150 	C) 8V and 16W\n")
if q5 == "C" or q5 == "c":
    print("Correct!")
    score += 1
else:
    print("incorrect!")

q6 = raw_input("Lamp is labelled 12V 36W. What current will it take on 12V supply and what is its resistance?\n"
               "Choose:  A) 3A and 4 ohms. 	B) 3A and 4 ohms 	C) 3A and 3 ohms\n")
if q6 == "B" or q6 == "b":
    print("Correct!")
    score += 1
else:
    print("incorrect!")

q7 = raw_input("What is the printed code for the following resistor? 100 ohm and 5% tolerance\n"
               "Choose:  A) Black Brown Brown Gold. 	B) Brown Black Red Gold 	C) Brown Black Brown Gold")
if q7 == "C" or q7 == "c":
    print("Correct!")
    score += 1
else:
    print("incorrect!")

q8 = raw_input("What is the printed code for the following resistor? 4.7k ohm and 2% tolerance\n"
               "Choose:  A) Orange Red Orange Red. 	B) Orange Violet Red Green 	C) Yellow Violet Red Red")
if q8 == "C" or q8 == "c":
    print("Correct!")
    score += 1
else:
    print("incorrect!")

q9 = raw_input("What is the printed code for the following resistor? 18k ohm and 1% tolerance\n"
               "Choose:  A) Gray Brown Orange Blue 	B) Brown Gray Orange Brown 	C) Brown Yellow Red Brown\n")
if q9 == "A" or q9 == "s":
    print("Correct!")
    score += 1
else:
    print("incorrect!")

q10 = raw_input("What is the printed code for the following resistor? 390k ohm and 20% tolerance\n"
                "Choose:  A) Orange White Yellow Gold. 	B) Red White Orange Gold 	C) Orange Blue Yellow Brown\n")
if q10 == "A" or q10 == "a":
    print("Correct!")
    score += 1
else:
    print("incorrect!")

q11 = raw_input("What's the electrical power dissipated in a 100 ohm resistor carrying a current of 50mA?\n"
                "Choose:  A) .25W. 	B) 5W 	C) 2.5W\n")
if q11 == "A" or q1 == "a":
    print("Correct!")
    score += 1
else:
    print("incorrect!")

q12 = raw_input("What's the wattage of a 6V 60mA lamp?\n"
                "Choose:  A) 3.6W. 	B) 10W 	C) .36W\n")
if q12 == "C" or q12 == "c":
    print("Correct!")
    score += 1
else:
    print("incorrect!")

q13 = raw_input("What is the charge stored when the voltage across a 100000 uF capacitor is 10V?\n"
                "Choose:  A) 1 Coulomb. 	B) .1 Coulomb 	C) 10 Coulombs\n")
if q13 == "A" or q13 == "a":
    print("Correct!")
    score += 1
else:
    print("incorrect!")

q14 = raw_input("What's the charge stored when the voltage across a 50 uF capacitor is 9V?\n"
                "Choose:  A) 45 uC. 	B) 450 uC 	C) 4500 uC\n")
if q14 == "B" or q14 == "b":
    print("Correct!")
    score += 1
else:
    print("incorrect!")

q15 = raw_input("Calculate the energy stored in a capacitor with a charge of 2C and 9V across its plates?\n"
                "Choose:  A) 18J. 	B) 4.5J 	C) 9J\n")
if q15 == "C" or q15 == "c":
    print("Correct!")
    score += 1
else:
    print("incorrect!")

q16 = raw_input("Calculate the energy stored in a 1uF capacitor charged to 500V\n"
                "Choose:  A) 12.5J 	B) 1.25J 	C) .125J\n")
if q16 == "C" or q16 == "c":
    print("Correct!")
    score += 1
else:
    print("incorrect!")

q17 = raw_input("Calculate the reactance of a 1uF capacitor at frequencies of 1KHz?\n"
                "Choose:  A) 109 ohms. 	B) 159 ohms 	C) 189 ohms\n")
if q17 == "B" or q17 == "b":
    print("Correct!")
    score += 1
else:
    print("incorrect!")

q18 = raw_input("What's the combined capacitance of a 2.2uF and 4.7uF in parallel?\n"
                "Choose:  A) 6.9uF. 	B) 1.5uF 	C) 3.45uF\n")
if q18 == "A" or q18 == "a":
    print("Correct!")
    score += 1
else:
    print("incorrect!")

q19= raw_input("What's the combined capacitance of two 100uF capacitors in series?\n"
               "Choose:  A) 200uF. 	B) 100uF 	C) 50uF\n")
if q19 == "C" or q19 == "c":
    print("Correct!")
    score += 1
else:
    print("incorrect!")

q20 = raw_input("What value of capacitance would give a reactance of 50 ohm at 700Hz?\n"
                "Choose:  A) 455uF. 	B) 4.55uF 	C) 45.5uF\n")
if q20 == "B" or q20 == "b":
    print("Correct!")
    score += 1
else:
    print("incorrect!")

time.sleep(0.1)
print("Your final score is: ")
print(score)
