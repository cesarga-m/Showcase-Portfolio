# CS 303E Mock Exam 1
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters
import math

# Problem 1: Poisson Probability
def poissonProbability():
    # write your solution to problem 1 here
    b = float(input())
    k = int(input())

    poisson = ((math.e ** (-1 * b)) * (b ** k)) / (math.factorial(k))
    print(format(poisson, ".3f"))

# Problem 2: Swap Case
def swapCase():
    # write your solution to problem 2 here
    y = input()
    x = int(ord(y))

    if 65 <= x <= 90:
        output = chr(ord(y) + 32)
        print(output)
    elif 97 <= x <= 122:
        output = chr(ord(y) - 32)
        print(output)
    else:
        print(y)


# Problem 3: Sum Series
def sumSeries():
    # write your solution to problem 3 here
    n = int(input())
    i = 2
    j = 0
    while i <= n:
        j = j + ((i - 1) * i)
        i = i + 1
    else:
        print(j)


# Problem 4: Sort Three Integers
def sortThreeIntegers():
    # write your solution to problem 4 here
    x = int(input())
    y = int(input())
    z = int(input())

    if x <= y <= z:
        print(x, y, z)
    elif x <= z <=y:
        print(x, z, y)
    elif y <= x <= z:
        print(y, x, z)
    elif y <= z <= x:
        print(y, z, x)
    elif z <= x <= y:
        print(z, x, y)
    elif z <= y <= x:
        print(z, y, x)


# Problem 5: Sum Positive Floats
def sumPositiveFloats():
    # write your solution to problem 5 here
    i = 1
    x = 0
    while True:
        i = i + 1
        y = float(input())
        if y > 0:
            x += y
        if y < 0:
            continue
        else:
            if i > 1 and y == 0:
                print(format(x, ".3f"))
                break
            elif i == 1 and y == 0:
                print(format(y, ".3f"))
                break


# Problem 6: Range Computation
def rangeComputation():
    # write your solution to problem 6 here
    start = int(input())
    end = int(input())
    check = 2
    total = start
    diff = start + 1
    for i in range((end - start)):
        total = total + diff
        diff = diff + 1
        if check == 3:
            total = total * 2
            check = 0
        check = check + 1
    print(total)

# Problem 7: Largest Square
def largestSquare():
    # write your solution to problem 7 here
    n = int(input())
    y = math.sqrt(n)
    print(math.floor(y))


# Problem 8: Collatz Conjecture
def collatzConjecture():
    # write your solution to problem 8 here
    n = int(input())
    terms = 0
    while True:
        if n == 1:
            terms += 1
            print(terms)
            break
        elif n % 2 == 0:
            n = n * (1 / 2)
            terms += 1
        else:
            n = 1 + n * 3
            terms += 1


if __name__=="__main__":
    """
    If you want to test your code on your computer, uncomment the respective
    function call(s) below.
    
    DO NOT CALL YOUR FUNCTIONS ANYWHERE OUTSIDE OF THIS AREA
    """

    # poissonProbability()
    # swapCase()
    # sumSeries()
    # sortThreeIntegers()
    # sumPositiveFloats()
    rangeComputation()
    # largestSquare()
    # collatzConjecture()


    # DO NOT DELETE THIS PASS
    pass
    # DON'T DO IT