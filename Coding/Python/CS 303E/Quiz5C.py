# CS 303E Quiz 5C
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters

# Problem 1: Nearby Scores
def nearbyScores(matrix, row, col):
    ns = 0
    p1 = abs(matrix[row-1][col-1]-matrix[row][col])
    p2 = abs(matrix[row-1][col+1]-matrix[row][col])
    p3 = abs(matrix[row-1][col]-matrix[row][col])
    p4 = abs(matrix[row][col-1]-matrix[row][col])
    p5 = abs(matrix[row][col+1]-matrix[row][col])
    p6 = abs(matrix[row+1][col-1]-matrix[row][col])
    p7 = abs(matrix[row+1][col+1]-matrix[row][col])
    p8 = abs(matrix[row+1][col]-matrix[row][col])

    if p1 <= 5:
        ns = ns + 1

    if p2 <= 5:
        ns = ns + 1

    if p3 <= 5:
        ns = ns + 1

    if p4 <= 5:
        ns = ns + 1

    if p5 <= 5:
        ns = ns + 1

    if p6 <= 5:
        ns = ns + 1

    if p7 <= 5:
        ns = ns + 1

    if p8 <= 5:
        ns = ns + 1

    return ns


# Problem 2: First Vowel Locations
def firstVowelLocations(strings):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    l = 0
    d = {}
    for j in strings:
        l = 0
        for i in j:
            if i in vowels:
                d[j] = l
                break
            l = l + 1
            if l == len(strings):
                d[j] = -1
    return d


if __name__ == '__main__':
    # uncomment the following lines to run the given test cases
    # note that the output will look slightly different
    # due to how the expected output is formatted

    # grid = [[100, 100, 97, 95, 77, 85, 82, 80, 95], [77, 57, 90, 84, 93, 100, 80, 74, 92], [70, 86, 82, 84, 64, 87, 100, 90, 97], [79, 77, 95, 80, 99, 81, 76, 68, 96], [66, 79, 73, 78, 87, 100, 78, 82, 81], [78, 85, 87, 80, 100, 90, 85, 88, 95], [75, 86, 75, 73, 76, 100, 100, 79, 85], [85, 70, 98, 73, 94, 84, 100, 92, 84], [85, 79, 76, 92, 85, 69, 78, 83, 88]]
    # print(nearbyScores(grid, 1, 2))
    # print(nearbyScores(grid, 7, 1))
    # grid2 = [[90, 87, 92, 77], [83, 94, 93, 100], [77, 81, 79, 89]]
    # print(nearbyScores(grid2, 1, 1))

    # print(firstVowelLocations({'apple', 'pteradactyl', 'bcdfghjklmnpqrstvwxyz'}))
    # print(firstVowelLocations({'GDC', 'ABC', '1two3four'}))
    # print(firstVowelLocations(set()))

    # DO NOT DELETE THIS PASS
    pass
    # DON'T DO IT