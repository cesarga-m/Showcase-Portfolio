# File: FindPrimeFactors.py
# Student: Cesar Gabriel Ayala-Mendoza
# UT EID: cga773
# Course Name: CS303E
#
# Date: 4/1/2022
# Description of Program: This program uses lists, functions, and loops to ask the user for a number and find its prime
# factorization, the program continues to ask for input until the user prompts the program to stop, it can deal with
# prime, composite, and negative numbers. If the number is a composite it returns a list of its prime factors, if the
# number is a prime it returns a list with only the respective number.

import math


def findNextPrime(num):
    if num < 2:
        return 2
# If (num >= 2 and num is even ), the
# next prime after num is at least
# (num - 1) + 2 , which is odd.
    if num % 2 == 0:
        num -= 1
    guess = num + 2
    while not isPrime(guess):
        guess += 2
    return guess


def isPrime(num):
    # Deal with evens and numbers < 2.
    if num < 2 or num % 2 == 0:
        return num == 2
    # See if there are any odd divisors
    # up to the square root of num.
    divisor = 3
    while divisor <= math.sqrt(num):
        if num % divisor == 0:
            return False
        else:
            divisor += 2
    return True


print("Find Prime Factors:")        # prints a welcome message before the loop starts


while True:
    num = int(input("Enter a positive integer (or 0 to stop): "))   # keeps asking the user for input
    primeList = [num]       # defaults the list to just the number inputted
    if num == 0:            # if user inputs 0 the program ends
        print("Goodbye!")
        break
    elif num < 0:           # prints message for negative numbers
        print("  Negative integer entered. Try again.")
        print()
    elif num == 1:          # prints message for the number 1
        print("  1 has no prime factorization.")
        print()
    elif num > 1:           # condition if the number is greater than 1
        if isPrime(num) is True:        # uses isPrime function, if number is prime a list with only the number is
            primeList = [num]           # printed

        elif isPrime(num) is False:     # if number is not prime, the list is set to a blank list and d is set to 2
            primeList = []
            d = 2
            opp = num                   # makes the operating number equal to the number inputted
            while True:
                if opp % d == 0:                # this loop checks if the operating number is divisible by d if it is,
                    primeList.append(d)         # it adds d to the list and sets the operating number to the quotient
                    opp = opp / d               # of the operating number divided by d
                else:
                    d = findNextPrime(d)        # when the operating number is no longer divisible by d, the value of d
                    if opp == 1:                # is changed to the next prime number by using the findNextPrime, the
                        break                   # loop continues until the operating number is equal to 1

        print("  The prime factorization of", num, "is:", primeList)   # prints a message with the number and its
        print()                                                       # prime factorization, then it asks for more input
