# File: Project2.py
# Student:
# UT EID:
# Course Name: CS303E
#
# Date:
# Description of Program:

def firstNFibNumbers():
    """ Return a list of the first n Fibonnaci numbers.  If
        n < 0, return the empty list. """
    n = int(input("You've asked for the first N Fibonnaci numbers. What is N? "))
    if n < 0:
        print(ERROR_V)
        return
    elif n == 0:
        print([])
        print()
        return
    # Handle the cases of n == 1 and n == 2 specially.
    elif n == 1:
        print([0])
        print()
        return
    elif n == 2:
        print([0, 1])
        print()
        return
    # Here we know that n is at least 2.
    else:
        # Initialize fib1 and fib2 with the first
        # two Fibonnaci numbers.
        fib1, fib2 = 0, 1
        # Initialize our list of Fibonnaci numbers
        # found so far.
        fibs = [0, 1]
        # Use the previous two values to generate
        # and record the next value.
        for counter in range(2, n):
            # Update fib1 and fib2 with their new
            # values.
            fib1, fib2 = fib2, fib1 + fib2
            # Add the newest value to the list we're
            # creating.
            fibs.append(fib2)
        print(fibs)     # print the list
        print()
        return


def ithFibNumber():
    n = int(input("You've asked for the ith Fibonnaci number. What is i? "))
    if n < 0:
        print(ERROR_V)  # handles case for when user inputs a negative number, returns error message
        return
    elif n == 0:
        print(0)
        print()
        return
    # Handle the cases of n == 1 and n == 2 specially.
    elif n == 1 or n == 2:
        print(1)
        print()
        return
    # Here we know that n is at least 2.
    else:
        # Initialize fib1 and fib2 with the first
        # two Fibonnaci numbers.
        fib1, fib2 = 0, 1
        # Initialize our list of Fibonnaci numbers
        # found so far.
        fibs = [0, 1]
        # Use the previous two values to generate
        # and record the next value.
        n = n + 1       # makes n larger so that the loop could run one more iteration and the n number can be sliced
        for counter in range(2, n):
            # Update fib1 and fib2 with their new
            # values.
            fib1, fib2 = fib2, fib1 + fib2
            # Add the newest value to the list we're
            # creating.
            fibs.append(fib2)
        print(fibs[n-1])    # prints the sliced element, ith number
        print()
        return


def numbersLessThanN():
    N = int(input("You've asked for the Fibonnaci numbers less than or equal to N. What is N? "))
    if N < 0:       # handles the negative numbers by returning an empty list
        print([])
        print()
        return
    elif N == 0:    # handles N == 0 by returning a list with only 0
        print([0])
        print()
        return
    # Handle the cases of n == 1 and n == 2 specially.
    elif N == 1:
        print([0, 1, 1])
        print()
        return
    elif N == 2:
        print([0, 1, 1, 2])
        print()
        return
    # Here we know that n is at least 2.
    else:
        # Initialize fib1 and fib2 with the first
        # two Fibonnaci numbers.
        fib1, fib2 = 0, 1
        # Initialize our list of Fibonnaci numbers
        # found so far.
        fibs = [0, 1]
        # Use the previous two values to generate
        # and record the next value.
        while True:
            # Update fib1 and fib2 with their new
            # values.
            fib1, fib2 = fib2, fib1 + fib2
            # Add the newest value to the list we're
            # creating.
            if fib2 > N:        # if the last fib2 is greater than N it stops appending, if it is still less the loop
                break           # keeps going and values are still added to the fibs list
            else:
                fibs.append(fib2)
        print(fibs)         # fibs list is printed with only values less than N
        print()
        return


def totalNumbersLessThanN():
    N = int(input("You've asked how many Fibonnaci numbers are less than or equal to N. What is N? "))
    if N < 0:       # handles the case of negative numbers by returning 0
        print(0)
        print()
        return
    elif N == 0:
        print(1)
        print()
        return
    # Handle the cases of n == 1 and n == 2 specially.
    elif N == 1:
        print(3)
        print()
        return
    elif N == 2:
        print(4)
        print()
        return
    # Here we know that n is at least 2.
    else:
        # Initialize fib1 and fib2 with the first
        # two Fibonnaci numbers.
        fib1, fib2 = 0, 1
        # Initialize our list of Fibonnaci numbers
        # found so far.
        fibs = [0, 1]
        # Use the previous two values to generate
        # and record the next value.
        while True:
            # Update fib1 and fib2 with their new
            # values.
            fib1, fib2 = fib2, fib1 + fib2
            # Add the newest value to the list we're
            # creating.
            if fib2 > N:    # if the last fib2 is greater than N it stops appending, if it is still less the loop
                break           # keeps going and values are still added to the fibs list
            else:
                fibs.append(fib2)
        print(len(fibs))    # length of fibs list is printed
        print()
        return


def sumFibToN():
    N = int(input("You've asked for Fibonnaci numbers that sum to N. What is N? "))
    if N < 0:   # handles the case of N being negative by returning an error
        print(ERROR_V)
        return
    elif N == 0:    # handles N == 0 by printing a list with only 0 on it
        print([0])
        print()
        return
    # Handle the cases of n == 1 and n == 2 specially.
    elif N == 1:
        print([0, 1])
        print()
        return
    elif N == 2:
        print([1, 1])
        print()
        return
    # Here we know that n is at least 2.
    else:
        # Initialize fib1 and fib2 with the first
        # two Fibonnaci numbers.
        fib1, fib2 = 0, 1
        # Initialize our list of Fibonnaci numbers
        # found so far.
        fibs = [0, 1]
        # Use the previous two values to generate
        # and record the next value.
        while True:
            # Update fib1 and fib2 with their new
            # values.
            fib1, fib2 = fib2, fib1 + fib2
            # Add the newest value to the list we're`
            # creating.
            if fib2 > N:        # if the last fib2 is greater than N it stops appending, if it is still less the loop
                break           # keeps going and values are still added to the fibs list
            else:
                fibs.append(fib2)

        i = -1          # used for the slicing of fibs
        fibsum = []         # creates empty list fibsum, list of the numbers that add up to N
        sum = 0         # initializes the sum as 0

        while True:
            if sum >= N:    # this stops the loop whenever the sum of the number of the sum list are greater than or
                break       # equal to N

            if (sum + fibs[i]) <= N:        # compares the sum of sum + fibs[i] to N, if this sum is less than N,
                fibsum.append(fibs[i])      # fib[i] is appended to the sum list

            i = i - 1       # changes i so that next time it slices, it slices the number before
            sum = 0         # resets the sum to 0

            for num in range(len(fibsum)):      # gets the sum of the fibsum list
                sum = sum + fibsum[num]

        print(fibsum)
        print()
        return


ERROR_C = "ERROR: Illegal command. Try again.\n"
ERROR_V = "ERROR: Illegal value entered.\n"
ZERO = "0"
ONE = "1"
TWO = "2"
THREE = "3"
FOUR = "4"
FIVE = "5"
SIX = "6"


print()
print("Welcome to the Fibonnaci Number laboratory!")
print()


def commandPrompts():
    print("The following commands are available:")
    print('''    0: Exit.
    1: List the first N Fibonnaci numbers.
    2: Display the ith Fibonnaci number (0-based).
    3: List the Fibonnaci numbers less or equal to N.
    4: How many Fibonnaci numbers are less or equal to N?
    5: Find a list of the largest Fibonnaci numbers that add up to N.
    6: Display this help message. 
    ''')
    return


commandPrompts()

while True:
    command = input("Please enter a command (0, 1, 2, 3, 4, 5 or 6): ")     #takes user input for command
    if command == ZERO:
        print()
        print("Thanks for using the Fibonnaci Laboratory!  Goodbye.")   # ends the program
        break
    elif command == ONE:
        firstNFibNumbers()
    elif command == TWO:
        ithFibNumber()
    elif command == THREE:                  # conditionals for the different commands by calling each different function
        numbersLessThanN()
    elif command == FOUR:
        totalNumbersLessThanN()
    elif command == FIVE:
        sumFibToN()
    elif command == SIX:
        commandPrompts()
        continue
    else:
        print(ERROR_C)              # shoots error message if command is invalid
        commandPrompts()
