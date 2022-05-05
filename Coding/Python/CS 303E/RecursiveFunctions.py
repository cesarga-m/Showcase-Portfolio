# File: RecursiveFunctions.py
# Student: Cesar Ayala-Mendoza
# UT EID: cga773
# Course Name: CS303E
#
# Date: 4/22/2022
# Description of Program: This program uses different recursive functions to return different values according to the
# different parameters and the details of each function.

def sumItemsInList(L):
    if L == []:     # if list is empty returns 0
        return 0
    else:
        return L[0] + sumItemsInList(L[1:])    # adds the 0th element and makes the list the numbers after that; repeats


def countOccurrencesInList(key, L):
    if L == []:     # if list is empty returns
        return 0
    elif key == L[0]:   # if key is equal to 0th element the count increases by one removes that element from list
        return 1 + countOccurrencesInList(key, L[1:])
    else:
        return countOccurrencesInList(key, L[1:])   # removes the current element if it is not equal to key


def addToN(n):
    if n == 0:  # if n is 0 it returns 0
        return 0
    if n >= 1:  # if n is greater than 1 n is added and function repeats with n decreasing by 1
        return n + addToN(n-1)


def findSumOfDigits(n):
    if n == 0:  # if n is 0 it returns 0
        return 0
    else:
        d = n % 10  # gets the last digit
        return findSumOfDigits(n // 10) + d     # adds digit, and changes function to n // 10 so it repeats


def integerToBinary(n):
    if n == 0 or n == 1:    # if n == 1 or 0 returns the string of n % 2
        return str(n % 2)
    else:
        sb = str(n % 2)     # sb is n % 2
        return integerToBinary(n//2) + sb   # changes n to n // 2 and adds sb, then repeats


def integerToList(n):
    ns = str(n)
    li = []
    if len(ns) == 1:    # if len of ns is 1 ns is appended and li is returned
        li.append(ns)
        return li
    if len(ns) > 1:     # if len of ns is still greater than 1 the 0th element of ns is appended and the new ns string
        li.append(ns[0])    # gets rid of that element, returns ns to an integer, so that li can be added to the
        ns = ns[1:]         # recursive function of the changed n
        n = int(ns)
        return li + integerToList(n)


def isPalindrome(s):
    end = len(s)        # the end is the len of s
    if end == 1 or end == 0:    # if end is 1 or 0 the string is palindrome, True is returned
        return True
    elif s[0] != s[end - 1]:    # if the 0th element is not the same to the last element of the list the string is not
        return False            # palindrome, False is returned
    else:
        return isPalindrome(s[1:end-1])     # function is repeated with the changed string


def findFirstUppercase(s):
    if s == "":     # if string is empty None is returned but not printed
        return None
    elif 65 <= ord(s[0]) <= 90:     # if the ascii value of the 0th element is between the uppercase values the it is
        return s[0]                 # the first uppercase
    else:
        return findFirstUppercase(s[1:])    # repeats the function with the changed string


def findFirstUppercaseIndexHelper(s, index):
    uc = findFirstUppercase(s)
    if uc is None:      # if the string does not have an uppercase the index is -1
        return -1
    if uc != s[0]:      # if the 0th element of the string is not the first uppercase the the index increases by 1
        index = index + 1
        return findFirstUppercaseIndexHelper(s[1:], index)  # changes the string and updates the index
    if uc == s[0]:      # if the 0th element is equal to the first uppercase the index is returned
        return index

# The following function is already completed for you.  But
# make sure you understand what it's doing.


def findFirstUppercaseIndex(s):     # calls the helper function with parameter s and index default to 0
    return findFirstUppercaseIndexHelper(s, 0)
