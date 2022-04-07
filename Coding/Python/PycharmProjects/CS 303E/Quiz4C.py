# CS 303E Quiz 4C
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters

# Problem 1: Condensed Communication
def condensedCommunication(str):
    # replace pass with your solution for Problem 1
    lstr = str.lower()
    nstr = ""
    for char in lstr:
        if 48 <= ord(char) <= 57 or 97 <= ord(char) <= 122:
            nstr = nstr + char
            fstr = nstr.strip()
    return fstr


# Problem 2: Adjacent Differences
def adjacentDifferences(lst):
    # replace pass with your solution for Problem 2
    difflist = []
    i = 0
    for j in range(len(lst)-1):
        difference = lst[i+1] - lst[i]
        difflist.append(difference)
        i = i + 1
    return difflist

if __name__ == "__main__":
    # uncomment the following lines to run the given test cases

    # print(condensedCommunication("Welp Stacy, I guess you're right. This truly is an ascended form of communication. You're just 3 smart 5 me."))
    # print(condensedCommunication("I wonder how long it will take you to decode this message..."))
    # print(condensedCommunication("Not 0nly is this so hard to understand, but I CAN'T EV3N 3MPHASIZ3 ANYTHING ANYMOR3!!!"))

    # print(adjacentDifferences([29, 15, 13, 20, 21, 1, 29, 6, 27, 28, 1, 6]))
    # print(adjacentDifferences([2, 3]))
    # print(adjacentDifferences([1, 2, 3, 4, 5, 5, 5, 4, 3, 2, 1]))
    pass
