# File: WordleAssistant.py
# Student: Cesar Ayala-Mendoza
# UT EID: cga773
# Course Name: CS303E
#
# Date: 4/16/2022
# Description of Program: This program reads through a document that has text on it, makes each line an element in a
# list, this list is filtered into words that are of a length of 5, 5 letter words that don't end in "s" and don't have
# any repeating letters. This list is used throughout the other functions that serve to narrow down this filtered list
# into sets of words that meet specific parameters.


def createWordlist(filename):
    wordsFile = open(filename, "r")
    wlst = []                       # opens the file from parameter, and makes line the reading of each line
    line = wordsFile.readline()
    wordleList = []

    while line:     # loop to go through each line and make that line an element in a list
        line = wordsFile.readline()
        wlst.append(line)

    for i in range(len(wlst)):      # gets rid of all the words that are not 5 letters long, the words are appended to
        if len(wlst[i]) == 6:       # a new list, "\n" is still a part of the words
            wordleList.append(wlst[i])

    ch = "\n"
    newWordleList = []
    newWord = ""

    for i in range(len(wordleList)):    # removes the \n by making a new string that does not contain "\n", this new
        word = str(wordleList[i])       # string is appended into a new list, the new string/word resets at the end
        for j in word:
            if j is not ch:
                newWord = newWord + j

        newWordleList.append(newWord)
        newWord = ""

    wordlist = []

    for i in range(len(newWordleList)):     # goes through each element of the list and makes this element a word, if
        word = str(newWordleList[i])        # word end with s it is not a part of the filtered list, if the word does
        if word[4] != "s":                  # not end in s it goes into a loop that checks each letter of the word, if a
            for j in word:                  # letter is not in the new word it is added to the new word; the new word
                if j not in newWord:        # was blank at first; this way if a letter repeats, it is not added to the
                    newWord = newWord + j   # new word, shortening the length of the new word, if the new word is still
            if len(newWord) == 5:           # the same length of 5 then this new word is appended to the filtered list.
                wordlist.append(newWord)
            newWord = ""

    count = len(wordlist)
    return wordlist, count


def containsAll(wordlist, include):
    """ Given your wordlist, return a set of all words from the wordlist
    that contain all of the letters in the string include.
    """

    inlist = []
    rlist = []
    i = 0
    count = 0

    for j in include:   # goes through each letter of the include string and it appends each letter into a different
        inlist.append(j)    # element in the inlist

    for j in wordlist:  # goes through each word in wordlist and then goes through each element in the inlist, if the
        for i in inlist:    # element is in the word the count increases by one, the the length of the inlist is
            if i in j:      # compared to the count, if they are equal the word is appended, the count resets at the end
                count = count + 1
        if count == len(inlist):
            rlist.append(j)
        count = 0

    inset = set(rlist)      # # makes the rlist a set, and returns this respective set
    return inset


def containsNone(wordlist, exclude):
    """ Given your wordlist, return a set of all words from the wordlist
    that do not contain any of the letters in the string exclude.
    """
    exlist = []
    rlist = []
    i = 0
    count = 0

    for j in exclude:   # goes through the string exclude and makes each letter an element in exlist
        exlist.append(j)

    for j in wordlist:  # goes through the words of wordlist and the goes through the letters in exlist, if the letter
        for i in exlist:    # is in the word the count increases by 1, when the second loop ends it compares the count
            if i not in j: # to the length of exlist, if it's the same the word is appended, regardless the count resets
                count = count + 1
        if count == len(exlist):
            rlist.append(j)
        count = 0

    exset = set(rlist)  # makes the rlist a set, and returns this respective set
    return exset


def containsAtPositions(wordlist, posInfo):
    """ posInfo is a dictionary that maps letters to positions.
    You can assume that the positions are in [0..4].  Return a set of
    all words from the wordlist that contain the letters from the
    dictionary at the indicated positions. For example, given posInfo
    {'a': 0, 'y': 4}.   This function might return the set:
    {'angry', 'aptly', 'amply', 'amity', 'artsy', 'agony'}. """
    pset = set()
    letter = []
    position = []

    for i in posInfo.values():  # gets values from posInfo and appends them to the letter list
        letter.append(i)

    for i in posInfo.keys():    # gets keys from posInfo and appends them to the position list
        position.append(i)

    for j in wordlist:      # goes through the words in wordlist and compares the position of the letters in the words
        if j[letter[0]] == position[0] and j[letter[1]] == position[1]: # if they match they are appended to pset
            pset.add(j)

    return pset


def getPossibleWords(wordlist, posInfo, include, exclude):
    """ Finally, given a wordlist, dictionary posInfo, and
    strings include and exclude, return the set of all words from
    the wordlist that contains the words that satisfy all of
    the following:
    * has letters in positions indicated in posInfo
    * contains all letters from string include
    * contains none of the letters from string exclude.
    """
    positionSet = containsAtPositions(wordlist, posInfo)
    containSet = containsAll(wordlist, include)             # calls functions to execute them with respective parameters
    excludeSet = containsNone(wordlist, exclude)

    satisfySet = containSet & excludeSet & positionSet  # creates a set that combines the similarities of control and
    return satisfySet  # exclude and position sets


