# File: Project1.py
# Student: Cesar Gabriel Ayala-Mendoza
# UT EID: cga773
# Course Name: CS303E
#
# Date: 2/24/2022
# Description of Program: This program uses all the material that has been covered in class so far, including functions,
# print statements, variables, math, if statements, and loops. The end goal of this program is to ask the user for input
# and according to that input perform a conversion from english to metric or metric to english. If the user fails to
# input what is acceptable an error message will shoot and the program will ask for the input again. Unless the user'
# quits the program in one of the prompts the program will continue running and will keep asking for inputs to perform
# conversions.

# Welcome statement
print('''
Welcome to the English/Metric conversion utility.

This utility allows you to convert between English units
(miles, feet, inches) and metric units (kilometers, meters,
centimeters).
''')

# Acceptable inputs for different selections set equal to variables for easier use in functions and loops
ONE = "1"
TWO = "2"
THREE = "3"

# Error message that will be shown when an invalid input is entered by the user
ERRORMESSAGE = "\nERROR: Answer must be 1, 2 or 3. Try again."

# Variables used in the program being defined so the IDE does not mark any problems with the program
englishString = 0
metricUnits = 0
englishUnits = 0

# Different functions that just serve as a bunch of print statements so that they save space in the loops and if
# statements


def beginning():
    print("------------------------------------------------------------")
    print()
    print("Which direction would you like to convert:")
    print("   For English to Metric type: 1")
    print("   For Metric to English type: 2")
    print("   To Quit type:               3")
    print()
    return


def english_metric():
    print()
    print("Select English units to convert to metric equivalent:")
    print("   For miles type:  1")
    print("   For feet type:   2")
    print("   For inches type: 3")
    print()
    return


def metric_selection():
    print()
    print("Convert to which metric units:")
    print("   For kilometers type:  1")
    print("   For meters type:      2")
    print("   For centimeters type: 3")
    print()
    return


def metric_english():
    print()
    print("Select metric units to convert to English equivalent:")
    print("   For kilometers type:  1")
    print("   For meters type:      2")
    print("   For centimeters type: 3")
    print()
    return


def english_selection():
    print()
    print("Convert to which English units:")
    print("   For miles type:  1")
    print("   For feet type:   2")
    print("   For inches type: 3")
    print()
    return

# The beginning loop that will take the users input and depending on the input it will enter other loops for each
# different type of conversion or if the input is not valid it will shoot the error message and prompt the user to
# provide an input that is acceptable. This is pretty much repetitive into the other loops until it gets to the line
# where the user must input the number of units desired to be converted into the other unit, a result is then printed
# and the program starts all over again until the user decides to quit.


while True:
    beginning()
    direction = input("   Input your answer (1, 2 or 3): ")
    if direction == ONE:
        while True:
            english_metric()
            englishUnits = input("   Choose English units to convert (1, 2 or 3): ")
            if englishUnits == ONE:
                while True:
                    englishString = "miles"
                    metric_selection()
                    metricUnits = input("   Choose target metric units (1, 2 or 3): ")
                    if metricUnits == ONE:
                        metricString = "kilometers"
                        print()
                        miles = float(
                            input("Enter the number of " + englishString + " to convert to " + metricString + ": "))
                        feet = miles * 5280
                        meters = 0.3048 * feet
                        kilometers = meters / 1000
                        print()
                        print("RESULT:", miles, englishString, "=", format(kilometers, ".3f"), metricString)
                        print()
                        break
                    elif metricUnits == TWO:
                        metricString = "meters"
                        print()
                        miles = float(
                            input("Enter the number of " + englishString + " to convert to " + metricString + ": "))
                        feet = miles * 5280
                        meters = 0.3048 * feet
                        print()
                        print("RESULT:", miles, englishString, "=", format(meters, ".3f"), metricString)
                        print()
                        break
                    elif metricUnits == THREE:
                        metricString = "centimeters"
                        print()
                        miles = float(
                            input("Enter the number of " + englishString + " to convert to " + metricString + ": "))
                        feet = miles * 5280
                        meters = 0.3048 * feet
                        centimeters = 100 * meters
                        print()
                        print("RESULT:", miles, englishString, "=", format(centimeters, ".3f"), metricString)
                        print()
                        break
                    else:
                        print(ERRORMESSAGE)
                break
            elif englishUnits == TWO:
                while True:
                    englishString = "feet"
                    metric_selection()
                    metricUnits = input("   Choose target metric units (1, 2 or 3): ")
                    if metricUnits == ONE:
                        metricString = "kilometers"
                        print()
                        feet = float(
                            input("Enter the number of " + englishString + " to convert to " + metricString + ": "))
                        meters = 0.3048 * feet
                        kilometers = meters / 1000
                        print()
                        print("RESULT:", feet, englishString, "=", format(kilometers, ".3f"), metricString)
                        print()
                        break
                    elif metricUnits == TWO:
                        metricString = "meters"
                        print()
                        feet = float(
                            input("Enter the number of " + englishString + " to convert to " + metricString + ": "))
                        meters = 0.3048 * feet
                        print()
                        print("RESULT:", feet, englishString, "=", format(meters, ".3f"), metricString)
                        print()
                        break
                    elif metricUnits == THREE:
                        metricString = "centimeters"
                        print()
                        feet = float(
                            input("Enter the number of " + englishString + " to convert to " + metricString + ": "))
                        meters = 0.3048 * feet
                        centimeters = 100 * meters
                        print()
                        print("RESULT:", feet, englishString, "=", format(centimeters, ".3f"), metricString)
                        print()
                        break
                    else:
                        print(ERRORMESSAGE)
                break
            elif englishUnits == THREE:
                while True:
                    englishString = "inches"
                    metric_selection()
                    metricUnits = input("   Choose target metric units (1, 2 or 3): ")
                    if metricUnits == ONE:
                        metricString = "kilometers"
                        print()
                        inches = float(
                            input("Enter the number of " + englishString + " to convert to " + metricString + ": "))
                        feet = inches / 12
                        meters = 0.3048 * feet
                        kilometers = meters / 1000
                        print()
                        print("RESULT:", inches, englishString, "=", format(kilometers, ".3f"), metricString)
                        print()
                        break
                    elif metricUnits == TWO:
                        metricString = "meters"
                        print()
                        inches = float(
                            input("Enter the number of " + englishString + " to convert to " + metricString + ": "))
                        feet = inches / 12
                        meters = 0.3048 * feet
                        print()
                        print("RESULT:", inches, englishString, "=", format(meters, ".3f"), metricString)
                        print()
                        break
                    elif metricUnits == THREE:
                        metricString = "centimeters"
                        print()
                        inches = float(
                            input("Enter the number of " + englishString + " to convert to " + metricString + ": "))
                        feet = inches / 12
                        meters = 0.3048 * feet
                        centimeters = 100 * meters
                        print()
                        print("RESULT:", inches, englishString, "=", format(centimeters, ".3f"), metricString)
                        print()
                        break
                    else:
                        print(ERRORMESSAGE)
                break
            else:
                print(ERRORMESSAGE)

    elif direction == TWO:
        while True:
            metric_english()
            metricUnits = input("   Choose metric units to convert (1, 2 or 3): ")
            if metricUnits == ONE:
                while True:
                    metricString = "kilometers"
                    english_selection()
                    englishUnits = input("   Choose target English units (1, 2 or 3): ")
                    if englishUnits == ONE:
                        englishString = "miles"
                        print()
                        kilometers = float(
                            input("Enter the number of " + metricString + " to convert to " + englishString + ": "))
                        meters = kilometers * 1000
                        feet = 3.28084 * meters
                        miles = feet / 5280
                        print()
                        print("RESULT:", kilometers, metricString, "=", format(miles, ".3f"), englishString)
                        print()
                        break
                    elif englishUnits == TWO:
                        englishString = "feet"
                        print()
                        kilometers = float(
                            input("Enter the number of " + metricString + " to convert to " + englishString + ": "))
                        meters = kilometers * 1000
                        feet = 3.28084 * meters
                        print()
                        print("RESULT:", kilometers, metricString, "=", format(feet, ".3f"), englishString)
                        print()
                        break
                    elif englishUnits == THREE:
                        englishString = "inches"
                        print()
                        kilometers = float(
                            input("Enter the number of " + metricString + " to convert to " + englishString + ": "))
                        meters = kilometers * 1000
                        feet = 3.28084 * meters
                        inches = feet * 12
                        print()
                        print("RESULT:", kilometers, metricString, "=", format(inches, ".3f"), englishString)
                        print()
                        break
                    else:
                        print(ERRORMESSAGE)
                break
            elif metricUnits == TWO:
                while True:
                    metricString = "meters"
                    english_selection()
                    englishUnits = input("   Choose target English units (1, 2 or 3): ")
                    if englishUnits == ONE:
                        englishString = "miles"
                        print()
                        meters = float(
                            input("Enter the number of " + metricString + " to convert to " + englishString + ": "))
                        feet = 3.28084 * meters
                        miles = feet / 5280
                        print()
                        print("RESULT:", meters, metricString, "=", format(miles, ".3f"), englishString)
                        print()
                        break
                    elif englishUnits == TWO:
                        englishString = "feet"
                        print()
                        meters = float(
                            input("Enter the number of " + metricString + " to convert to " + englishString + ": "))
                        feet = 3.28084 * meters
                        print()
                        print("RESULT:", meters, metricString, "=", format(feet, ".3f"), englishString)
                        print()
                        break
                    elif englishUnits == THREE:
                        englishString = "inches"
                        print()
                        meters = float(
                            input("Enter the number of " + metricString + " to convert to " + englishString + ": "))
                        feet = 3.28084 * meters
                        inches = feet * 12
                        print()
                        print("RESULT:", meters, metricString, "=", format(inches, ".3f"), englishString)
                        print()
                        break
                    else:
                        print(ERRORMESSAGE)
                break
            elif metricUnits == THREE:
                while True:
                    metricString = "centimeters"
                    english_selection()
                    englishUnits = input("   Choose target English units (1, 2 or 3): ")
                    if englishUnits == ONE:
                        englishString = "miles"
                        print()
                        centimeters = float(
                            input("Enter the number of " + metricString + " to convert to " + englishString + ": "))
                        meters = centimeters / 100
                        feet = 3.28084 * meters
                        miles = feet / 5280
                        print()
                        print("RESULT:", centimeters, metricString, "=", format(miles, ".3f"), englishString)
                        print()
                        break
                    elif englishUnits == TWO:
                        englishString = "feet"
                        print()
                        centimeters = float(
                            input("Enter the number of " + metricString + " to convert to " + englishString + ": "))
                        meters = centimeters / 100
                        feet = 3.28084 * meters
                        print()
                        print("RESULT:", centimeters, metricString, "=", format(feet, ".3f"), englishString)
                        print()
                        break
                    elif englishUnits == THREE:
                        englishString = "inches"
                        print()
                        centimeters = float(
                            input("Enter the number of " + metricString + " to convert to " + englishString + ": "))
                        meters = centimeters / 100
                        feet = 3.28084 * meters
                        inches = feet * 12
                        print()
                        print("RESULT:", centimeters, metricString, "=", format(inches, ".3f"), englishString)
                        print()
                        break
                    else:
                        print(ERRORMESSAGE)
                break
            else:
                print(ERRORMESSAGE)
    elif direction == THREE:
        print()
        print("Thanks for using our converter. Goodbye!")
        break
    else:
        print(ERRORMESSAGE)
        print()
