# CS 303E Quiz 3C
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters
import math

# Problem 1: Root Parity Rule
def followsRule(num):
    sqr = math.floor(math.sqrt(num))
    if sqr % 2 == 0:
        y = "True"
        return y
    else:
        y = "False"
        return y
    pass


def rangeOfNums(lower, upper):
    min = lower
    max = upper
    i = 0
    while True:
        sqr = math.floor(math.sqrt(min))
        if sqr % 2 == 0:
            i = i + 1
        min = min + 1
        if min > max:
            break
    return i

    pass



# Problem 2: Phone Bill Class
class PhoneBill:
    # REMEMBER TO MAKE YOUR DATA MEMBERS PRIVATE
    def __init__(self, carrier, rate, minutes):
        self.carrier = carrier
        self.rate = rate
        self.minutes = minutes
        pass

    def makeCall(self, minutes):
        smins = self.minutes
        self.minutes = minutes
        self.minutes = smins + self.minutes
        pass

    def switchCarrier(self, carrier, rate):
        self.carrier = carrier
        self.rate = rate
        pass

    def getBill(self):
        self.getBill = self.minutes * self.rate * 0.01
        return "$" + str(format(self.getBill, ".2f"))
        pass

    def __str__(self):
        return "The phone bill under" + str(self.carrier) + "for this month is $" + str(format(self.getBill, ".2f"))
        pass


if __name__ == '__main__':
    # uncomment the following lines to run the given test cases
    # note that the output will look slightly different
    # due to how the expected output is formatted

    # print(followsRule(5))
    # print(followsRule(15))
    # print(rangeOfNums(0, 10))

    # pb = PhoneBill("TMobile", 67, 0)
    # print(pb.getBill())

    # pb = PhoneBill("AT&T", 71, 530)
    # pb.makeCall(20)
    # print(pb)

    # pb = PhoneBill("Verizon", 72, 340)
    # pb.makeCall(15)
    # pb.switchCarrier("AT&T", 71)
    # pb.makeCall(15)
    # print(pb)

    # DO NOT DELETE THIS PASS
    pass
    # DON'T DO IT