# File: Project3.py
# Student: Cesar Gabriel Ayala-Mendoza
# UT EID: cga773
# Course Name: CS303E
#
# Date: 4/26/2022
# Description of Program:


import os.path
import random


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


print('''
Welcome to WORDLE, the popular word game. The goal is to guess a
five letter word chosen at random from our wordlist.  None of the
words on the wordlist have any duplicate letters.

You will be allowed 6 guesses.  Guesses must be from the allowed
wordlist.  We'll tell you if they're not.

Each letter in your guess will be marked as follows:

   x means that the letter does not appear in the answer
   ^ means that the letter is correct and in the correct location
   + means that the letter is correct, but in the wrong location

Good luck!
''')

ERRORF = "File does not exist. Try again!"
ERRORW = "Guess must be a 5-letter word in the wordlist.  Try again!"


def BinarySearch(lst, key):         # Binary Search function
    low = 0
    high = len(lst) - 1
    while high >= low:
        mid = (low + high) // 2
        if key < lst[mid]:
            high = mid - 1
        elif key == lst[mid]:
            return mid
        else:
            low = mid + 1
    return - low - 1


while True:
    file = input("Enter the name of the file from which to extract the wordlist: ")     # takes name of file
    if not os.path.isfile(file):    # checks is file exists, if it doesn't an error message is shown
        print(ERRORF)
    else:
        print()
        break

wordlist, count = createWordlist(file)
wlist = wordlist
gw = random.choice(wlist)       # gets a random word from the wordlist

for i in range(1, 7):
    g = str(i)
    while True:
        word = input("Enter your guess (" + g + "): ")      # takes the guess and makes it lowercase
        word = word.lower()
        if BinarySearch(wlist, word) < 0:   # looks for the guess in the wordlist and keeps asking user for
            print(ERRORW)                   # input if word is not in the wordlist and prints error message
        if word in wlist:
            break

    for j in word:      # displays the word with capital letters
        letter = j.upper()
        print(letter, end="  ")
    print()

    k = 0

    while True:         # loop to compare the letters from the guess to the word
        le = word[k]
        ch = gw[k]
        while True:
            if le in gw and le is ch:   # if the letter is in the word and the letter is in the right position the
                print("^", end="  ")    # carrot is printed in that position
                break
            elif le in gw and le is not ch:     # if the letter is in the word but not in the right position the plus
                print("+", end="  ")            # is printed in that position
                break
            else:
                print("x", end="  ")    # if the letter is not in the word then an x is printed
                break
        k = k + 1
        if k == 5:      # this breaks the loop when the letters are done comparing
            break

    if word == gw:      # if the words are the same a congratulations message is printed and program ends
        print("\nCONGRATULATIONS! You win!")
        break

    print()

    if i == 6 and word != gw:   # if the player had the 6 guesses and did not guess correct the message is printed
        print("\nSorry!  The word was " + gw + ". Better luck next time!")      # and program ends
