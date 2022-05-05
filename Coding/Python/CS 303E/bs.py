def characterLastIndexDictionary(string, index):
    # replace pass with your solution to problem 7 here
    if index > len(string) - 1:
        return
    n = string[index]
    dic = {n: index}
    print(dic)
    return dic[characterLastIndexDictionary(string, index+1)]

print(characterLastIndexDictionary('Hello World!', 0))