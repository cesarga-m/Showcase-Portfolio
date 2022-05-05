# CS 303E Quiz 1D
# do NOT rename this file, otherwise Gradescope will not accept your submission
import math

# Problem 1: Optimal Stats
def optimalStats():
    # write your solution to problem 1 here
    attack = float(input())
    critical_rate = float(input())
    critical_damage = float(input())
    power = math.sqrt((attack / 10) ** 3) + (((critical_rate * critical_damage) / (critical_rate + 1)) ** 2) + 1
    print(format(power, ".2f"))



# Problem 2: Apple Juice
def appleJuice():
    # write your solution to problem 2 here
    small_apples = float(input())
    medium_apples = float(input())
    large_apples = float(input())
    total_juice = (small_apples * 0.12) + (medium_apples * 0.35) + (large_apples * 0.63)
    print(math.floor(total_juice))

if __name__=="__main__":
    """
    If you want to test your code on your computer, uncomment the respective
    function call(s) below.
    
    DO NOT CALL YOUR FUNCTIONS ANYWHERE OUTSIDE OF THIS AREA
    """
    # optimalStats()
    # appleJuice()

    # DO NOT DELETE THIS PASS
    pass
    # DON'T DO IT