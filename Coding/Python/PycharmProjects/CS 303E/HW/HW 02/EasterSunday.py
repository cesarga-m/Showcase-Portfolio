# File: EasterSunday.py
# Student: Cesar Gabriel Ayala-Mendoza
# UT EID: cga773
# Course Name: CS3003E
#
# Date: 2/3/2022
# Description of Program: This program uses variables to store mathematical operations to complete an algorithm that was
# invented by Carl Gauss. This mathematician designed an algorithm that finds when Easter Sunday took place for a
# specified year.

# The user is asked to input a year and stores it as an integer which equals variable y
y = int(input("Enter year: "))
a = y % 19
b = y // 100
c = y % 100
d = b // 4
e = b % 4
g = (8 * b + 13) // 25
h = (19 * a + b - d - g + 15) % 30
j = c // 4
k = c % 4
m = (a + 11 * h) // 319
r = (2 * e + 2 * j - k - h + m + 32) % 7
n = (h - m + r + 90) // 25
p = (h - m + r + n + 19) % 32

# After the above mathematical equations from the Gauss' algorithm are performed and set equal to certain variables the
# last variables "n" and "p" represent to month and the day respectively. The print function below outputs the result of
# the algorithm by saying that in "y" the entered year Easter Sunday was on month "n" and day "p."
print("In", y, "Easter Sunday is on month", n, "and day", p,)
