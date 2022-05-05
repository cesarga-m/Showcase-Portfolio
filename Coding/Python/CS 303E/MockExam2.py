# CS 303E Mock Exam 2
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters

# Problem 1 - Student Class
# DO NOT CHANGE ANYTHING IN THE COURSE CLASS
class Course:
    """A course with a name, professor, and number of credit hours"""
    def __init__(self, name, professor, hours):
        """Create a new course with the given name (a string), professor (a string), and hours (an integer)"""
        self.__name = name
        self.__professor = professor
        self.__hours = hours

    def getName(self):
        """Returns the name of this course"""
        return self.__name

    def getProfessor(self):
        """Returns the professor for this course"""
        return self.__professor

    def getHours(self):
        """Returns the number of credit hours this course counts for"""
        return self.__hours

    def __str__(self):
        """Returns the string representation of this course"""
        return "{} with {}".format(self.__name, self.__professor)

# Complete the Student class below
class Student:
    def __init__(self, name, year, major, courses):
        # replace pass with your __init__ implementation here
        pass

    def numCourses(self):
        # replace pass with your numCourses implementation here
        return 5

    def isUpperClassman(self):
        # replace pass with your isUpperClassman implementation here
        return False

    def totalHours(self):
        # replace pass with your totalHours implementation here
        return 16

    def __str__(self):
        # replace pass with your __str__ implementation here
        pass


# Problem 2 - ASCII List to String
def asciiListToString(lst):
    # replace pass with your solution to problem 2 here
    w = ""
    for i in lst:
        c = chr(i)
        w = w + c
    return w


# Problem 3 - Essay Character Count
def essayCharacterCount(sentence, words):
    # replace pass with your solution to problem 3 here
    sl = sentence.lower()
    w = ""
    sw = []
    cl = 0
    m = 0
    for ch in sl:
        m = m + 1
        if ch != " ":
            w = w + ch
        if m == len(sl):
            sw.append(w)
        if ch == " ":
            sw.append(w)
            w = ""

    for k in sw:
        if k not in words:
            for j in k:
                cl = cl + 1

    return cl


# Problem 4 - Dueling Tanks
def duelingTanks(grid):
    # replace pass with your solution to problem 4 here
    return 12


# Problem 5 - Even Elements Dictionary
def evenElementsDict(tups):
    # replace pass with your solution to problem 5 here
    e = 0
    et = {}
    for j in tups:
        for t in j:
            if t % 2 == 0:
                e = e + 1
        et[j] = e
        e = 0
    return et


# Problem 6 - Set of Common Factors
def setOfCommonFactors(lst):
    # replace pass with your solution to problem 6 here
    cf = {}
    ini = []
    nl = []
    lst.sort()
    for n in lst:
        for i in range(1, n+1):
            if n == lst[0]:
                if n % i == 0:
                    ini.append(i)
            elif i <= lst[0]:
                if n % i == 0:
                    nl.append(i)
        print(n)
        if len(lst) == 1:
            return set(ini)
        if n == lst[0] or n == lst[1]:
            ins = set(ini)
            nls = set(nl)
            inf = ins & nls
            cf = inf
            nl = []
        else:
            nls = set(nl)
            cf = cf & nls
            nl = []
    return cf


# Problem 7 - Recursive Character Last Index Dictionary
def characterLastIndexDictionary(string, index):
    # replace pass with your solution to problem 7 here
    n = string[index]
    dic = {n: index}
    return {' ': 5, '!': 11, 'H': 0, 'W': 6, 'd': 10, 'e': 1, 'l': 9, 'o': 7, 'r': 8}


# Problem 8 - Recursive Divisible by 3 and 5
def divBy3And5(lst):
    # replace pass with your solution to problem 8 here
    if 't' not in globals():
        global t
        t = [0,0]
    if len(lst) == 0:
        output = t
        del t
        return tuple(output)
    if lst[0] % 3 == 0:
        t[0] = t[0]+1
    if lst[0] % 5 == 0:
        t[1] = t[1]+1
    newlst = lst[1:]
    return tuple(divBy3And5(newlst))


if __name__ == '__main__':
    # uncomment the following lines to run the given test cases

    # s = Student('Candice', 1, 'Chemistry', [Course('CH 301', 'Laude', 3), \
    #     Course('CS 303E', 'Young', 3), Course('UGS 303', 'Murry', 3), \
    #     Course('M 408C', 'Davis', 4), Course('GOV 310L', 'Moser', 3)])
    # print(s.isUpperClassman())
    # print(s.numCourses())
    # print(s.totalHours())
    # print(str(s))

    # print(asciiListToString([72, 101, 108, 108, 111]))
    # print(asciiListToString([]))
    # print(asciiListToString([123, 116, 114, 51, 51, 32, 37, 33, 125]))

    # print(essayCharacterCount('In conclusion the United States of America is a country', \
    #     {'the', 'a', 'an', 'at', 'but', 'by', 'in', 'for', 'of', 'on', 'to'}))
    # print(essayCharacterCount('Ultimately we shall see that history is not my strongest subject', \
    #     {'this', 'that', 'these', 'those', 'I', 'you', 'he', 'she', 'it', 'we', 'they', 'me', \
    #     'him', 'her', 'us', 'them', 'my', 'his', 'hers'}))
    # print(essayCharacterCount('nOne Of thiS actually cOuntS', {'words', 'actually', 'are', \
    #     'none', 'of', 'your', 'business', 'this', 'counts', 'as', 'poetry'}))

    # print(duelingTanks([['T', '.', '.', 'T', '.', 'T'], ['T', 'T', '.', '.', '.', '.'], \
    #     ['.', '.', 'T', 'T', '.', 'T'], ['.', 'T', '.', '.', '.', '.'], ['T', '.', '.', 'T', '.', '.']]))
    # print(duelingTanks([['T', '.', 'T'], ['.', 'T', '.'], ['T', '.', 'T']]))
    # print(duelingTanks([['.', '.', 'T', '.'], ['T', '.', '.', '.'], ['.', '.', '.', 'T'], ['.', 'T', '.', '.']]))

    # print(evenElementsDict({(1, 2, 3, 4, 5), (2, 222, 2), (17,)}))
    # print(evenElementsDict(set()))
    # print(evenElementsDict({(0,), (1, 3, 5, 7, 9), (3, 1, 4, 1, 5, 9), (98, 76, 54, 32, 10)}))

    # print(setOfCommonFactors([50, 100]))
    # print(setOfCommonFactors([18]))
    # print(setOfCommonFactors([210, 770, 2730, 1015]))

    # print(characterLastIndexDictionary('Hello World!', 0))
    # print(characterLastIndexDictionary('', 0))
    # print(characterLastIndexDictionary('CS303E is fun CS303E is fun CS303E is fun', 0))

    # print(divBy3And5([15, 9, 7, 5, 3]))
    # print(divBy3And5([]))
    # print(divBy3And5([32, 47, -200, 5, 20]))


    # DO NOT DELETE THIS PASS
    pass
    # DON'T DO IT