# CS 303E Exam 1C
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters
import math

# Problem 1: Cupcake Baking
def cakeBaking():
    # write your solution to problem 1 here
    e = int(input())
    b = float(input())
    bp = float(input())

    en = 3
    bn = 1.4
    bpn = 2.3

    ae = math.floor(e / en)
    ab = math.floor(b / bn)
    abp = math.floor(bp / bpn)

    if ae <= ab and ae <= abp:
        print(ae)
    elif ab <= ae and ab <= abp:
        print(ab)
    elif abp <= ae and abp <= ab:
        print(abp)

# Problem 2: Daily Wages
def dailyWages():
    # write your solution to problem 2 here
    dw = int(input())
    total = 0
    while True:
        d = input()
        if d == "work":
            total = total + dw
        elif d == "rest":
            total = total + 0
        elif d == "raise":
            total = total + dw
            dw = dw + 1
        elif d == "end":
            print(total)
            break


# Problem 3: Holiday Decorations
def holidayDecorations():
    # write your solution to problem 3 here
    m = int(input())
    d = int(input())

    if 11 <= m <= 12:
        print("Valentine's Day")
    elif m == 1:
        print("Valentine's Day")
    elif m == 2 and d <= 14:
        print("Valentine's Day")
    elif m == 2 and d > 14:
        print("Fourth of July")
    elif 3 <= m <= 6:
        print("Fourth of July")
    elif m == 7 and d <= 4:
        print("Fourth of July")
    else:
        print("Halloween")


# Problem 4: Closest to Given Price
def closestPrice():
    # write your solution to problem 4 here
    n = int(input())
    diff = 9999999999999999999999999999999999999999999999999999999999999999999
    i = 0
    b = 0
    c = diff

    for j in range(n):
        p = float(input())
        diff = math.fabs(15 - p)
        i = i + 1
        if diff <= c:
            c = diff
            b = i

    print(b)

# Problem 5: Next Letter
def nextLetter():
    # write your solution to problem 5 here
    l = input()
    al = int(ord(l))
    al1 = al + 1
    o = chr(al1)

    if al == 90:
        o = "A"
    elif al == 122:
        o = "a"

    print(o)

# Problem 6: Small Average
def smallAverage():
    # write your solution to problem 6 here
    k = float(input())
    t = int(input())
    i = 0
    a = 0

    while i < t:
        n = i + 1
        i = i + 1
        a = a + ((n - 1) * math.sqrt(n)) ** 3
    else:
        an = (1 / t) * a
        if an <= k:
            print(format(an, ".3f"))
        elif an > k:
            print("TOO BIG!")



# Problem 7: Free Throw Contest
def freeThrowContest():
    # write your solution to problem 7 here
    r1 = int(input())
    r2 = int(input())
    r3 = int(input())
    r4 = int(input())
    r5 = int(input())
    b = 0

    if r1 + r2 + r3 >= 30 or r1 + r2 + r4 >= 30 or r1 + r2 + r5 >= 30:
        b = 15
    elif r1 + r4 + r5 >= 30 or r1 + r3 + r4 >= 30 or r1 + r3 + r5 >= 30:
        b = 15
    elif r2 + r3 + r4 >= 30 or r2 + r3 + r5 >= 30 or r3 + r4 + r5 >= 30 or r2 + r4 + r5 >= 30:
        b = 15

    total = r1 + r2 + r3 + r4 + r5 + b
    print(total)


# Problem 8: Increasing Pair Values
def increasingPairValues():
    # write your solution to problem 8 here
    while True:
        c = input()
        if c == "X":
            print(0)
            break




if __name__=="__main__":
    """
    If you want to test your code on your computer, uncomment the respective
    function call(s) below.

    DO NOT CALL YOUR FUNCTIONS ANYWHERE OUTSIDE OF THIS AREA
    """

    # cakeBaking()
    # dailyWages()
    holidayDecorations()
    # closestPrice()
    # nextLetter()
    # smallAverage()
    # freeThrowContest()
    # increasingPairValues()

    # DO NOT DELETE THIS PASS
    pass
    # DON'T DO IT