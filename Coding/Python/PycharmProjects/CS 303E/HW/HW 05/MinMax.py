# File: MinMax.py
# Student: Cesar Gabriel Ayala-Mendoza
# UT EID: cga773
# Course Name: CS303E
#
# Date: 2/24/2022
# Description of Program: In this program the user is asked to input an integer and with the use of a while loop it
# keeps asking the user for inputs until the user inputs "stop". The input values are converted to integers so that
# inside the loop the integers can be compared to determine the minimum and maximum integers. The output tells the user
# which of the values that were inputted are the minimum and maximum integers.

# This first line takes the input of the user and stores it as a variable.
int_value = (input("Enter an integer or 'stop' to end: "))


# This if statement accounts for when the user enters "stop" as the first input before inputting any actual number
# values, it makes it so that it lets the user know that he did not enter any number values, and the program ends there.
if int_value == "stop":
    print("You didn't enter any numbers")

# If the user's first input was not "stop" this part of the program can run, the first section of the else statement
# changes the string from the first input to an integer value and gives the minimum and maximum integers an initial
# value so the first input line of the while loop does not get rid of the first input.
else:
    integer = int(int_value)
    minimum_int = integer
    maximum_int = integer
    # The loop starts here and the condition for it to keep running is that the user does not input "stop", if the user
    # does not input "stop" it keeps asking the user for an input.
    while int_value != "stop":
        int_value = (input("Enter an integer or 'stop' to end: "))
        if int_value == "stop":                             # When the user inputs "stop" the loop stops and it prints
            print("The maximum is ", maximum_int, sep="")   # what the maximum and minimum integer values are and the
            print("The minimum is ", minimum_int, sep="")   # program ends here.
        else:
            integer = int(int_value)    # If the user has not inputted stop this else block will run and it will keep
            if integer > maximum_int:   # converting the user inputs into integers so that they can be compared to the
                maximum_int = integer   # current minimum and maximum that have been inputted. If the most recent
            if integer < minimum_int:   # integer is more than the maximum it becomes the new maximum, or if it is less
                minimum_int = integer   # than the minimum it becomes the new minimum. After this the loop continues.
