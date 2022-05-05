# File: MyStringFunctions.py
# Student: Cesar Gabriel Ayala-Mendoza
# UT EID: cga773
# Course Name: CS303E
#
# Date: 3/28/2022
# Description of Program: Functions that use different string functions and methods to return values according to the
# different parameters.


def myAppend(str, ch):
    # Return a new string that is like str but with
    # character ch added at the end
    return str + ch


def myCount(str, ch):
    # Return the number of times character ch appears
    # in str.
    n = 0
    i = 0
    for i in range(len(str)):
        if ch == str[i]:
            n = n + 1
        i = i + 1
    return n


def myExtend(str1, str2):
    # Return a new string that contains the elements of
    # str1 followed by the elements of str2, in the same
    # order they appear in str2.
    return str1 + str2


def myMin(str):
    # Return the character in str with the lowest ASCII code.
    # If str is empty, print "Empty string: no min value"
    # and return None.
    i = 0
    mini = 128

    if str == "":
        return print("Empty string: no min value")
    else:
        for i in range(len(str)):
            ch = int(ord(str[i]))
            i = i + 1

            if ch < mini:
                mini = ch

        return chr(mini)


def myInsert(str, i, ch):
    # Return a new string like str except that ch has been
    # inserted at the ith position.  I.e., the string is now
    # one character longer than before. Print "Invalid index" if
    # i is greater than the length of str and return None.
    length = len(str)
    j = 0
    if i > length:
        return print("Invalid index")
    else:
        for j in range(len(str)):
            if j == i:
                break
            j = j + 1
        return str[:j] + ch + str[j:]


def myPop(str, i):
    # Return two results:
    # 1. a new string that is like str but with the ith
    #    element removed;
    # 2. the value that was removed.
    # Print "Invalid index" if i is greater than or
    # equal to len(str), and return str unchanged and None
    length = len(str)
    j = 0
    if i >= length:
        return str, print("Invalid index")
    else:
        for j in range(len(str)):
            if i == j:
                break
            j = j + 1
        return str[:j] + str[j+1:], str[j]


def myFind(str, ch):
    # Return the index of the first (leftmost) occurrence of
    # ch in str, if any.  Return -1 if ch does not occur in str.
    i = 0
    f = -1
    for i in range(len(str)):
        if ch == str[i]:
            f = i
            break
        i = i + 1
    return f


def myRFind(str, ch):
    # Return the index of the last (rightmost) occurrence of
    # ch in str, if any.  Return -1 if ch does not occur in str.
    i = 0
    f = -1
    for i in range(len(str)):
        if ch == str[i]:
            f = i
        i = i + 1
    return f


def myRemove(str, ch):
    # Return a new string with the first occurrence of ch
    # removed.  If there is none, return str.
    product = ""
    i = 0
    if ch not in str:
        return str
    else:
        for i in range(len(str)):
            if ch is str[i]:
                break
            i = i + 1
        return str[:i] + str[i+1:]


def myRemoveAll(str, ch):
    # Return a new string with all occurrences of ch.
    # removed.  If there are none, return str.
    product = ""
    if ch not in str:
        return str
    else:
        for i in str:
            if i is not ch:
                product = product + i
        return product


def myReverse(str):
    # Return a new string like str but with the characters
    # in the reverse order.
    reverse = ""
    if len(str) == 0:
        return str
    else:
        for i in str:
            reverse = i + reverse
        return reverse
