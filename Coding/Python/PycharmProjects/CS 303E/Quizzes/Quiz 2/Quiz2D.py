# CS 303E Quiz 2D
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters
import math

# Problem 1: Advanced Rock Collector Days Needed
def rockCollector():
    R1 = float(input())
    days = 1
    R2 = 1.63 * days ** 3 - days
    if R2 > R1:
        days = 1
    while R2 < R1:
        R2 = 1.62 * days ** 3 - days
        R2 += R2
        days = days + 1
    else:
        print(days)


# Problem 2: Candy Purchases
def candyPurchases():
    # write your solution to problem 2 here
    CandyCane = 3.25
    lolli = 5.97
    choco = 2
    caramel = 4.3
    gummies = 1.89
    result = 0
    a = input()
    b = input()

    if a == "Candy Cane" and b == "Lollipop":
        result = CandyCane + lolli
        print("$", result, sep="")
    if a == "Caramel" and b == "Gummies":
        result = caramel + gummies
        print("$", result, sep="")
    if a == "Lollipop" and b == "Chocolate":
        print("$", result, sep="")

if __name__=="__main__":
    """
    If you want to test your code on your computer, uncomment the respective
    function call(s) below.
    
    DO NOT CALL YOUR FUNCTIONS ANYWHERE OUTSIDE OF THIS AREA
    """

    #rockCollector()
    candyPurchases()


    # DO NOT DELETE THIS PASS
    pass
    # DON'T DO IT