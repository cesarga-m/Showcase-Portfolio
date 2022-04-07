# File: DaysInMonth.py
# Student: Cesar Gabriel Ayala-Mendoza
# UT EID: cga773
# Course Name: CS303E
#
# Date: 2/15/2022
# Description of Program: This program takes the input from the user and then outputs how many days there was in the
# that was entered and it also converts the integer that was entered as month to the name of the month. e.g. input = 1
# output = January & 31 days.


# This part of the code asks the user for its input, the first input line asks the user for the year and stores it as an
# integer in the variable "year". The second input line asks the user for the number of the month and stores it as an
# integer in the variable "month".
year = int(input("Please enter a year: "))
month = int(input("Please enter a month: "))

# This part of the code is just a buffer so that the variables can always store a certain value in case the user inputs
# other numbers that are not in the range of [1,12], this also helps my IDE not mark errors in my code.
monthname = "N/A"
days = "N/A"

# This part of the code uses if statements to change the value of the variables "monthname" and "days" when one of the
# integers inputted for the variable "month" is in the range of [1,12]. The "monthname" variable stores the name of the
# month as a string and the "days" variable stores the number of days in the month as a string, it is done according to
# the different months.
if month == 2:
    monthname = "February"
    days = "28"
    if year % 4 == 0:               # This section of the if statements is for determining whether the year is leap year
        days = "29"                 # or not, if it is the "days" variable stores the value of 29 days. A leap year
        if year % 100 == 0:         # needs to be divisible by 4, but then if it divisible by 100 it might not be a leap
            days = "28"             # unless it is also divisible by 400, this is why the value of the variable "days"
            if year % 400 == 0:     # alternates between these lines.
                days = "29"
elif month == 1:
    monthname = "January"
    days = "31"
elif month == 3:
    monthname = "March"
    days = "31"
elif month == 4:
    monthname = "April"
    days = "30"
elif month == 5:
    monthname = "May"
    days = "31"
elif month == 6:
    monthname = "June"
    days = "30"
elif month == 7:
    monthname = "July"
    days = "31"
elif month == 8:
    monthname = "August"
    days = "31"
elif month == 9:
    monthname = "September"
    days = "30"
elif month == 10:
    monthname = "October"
    days = "31"
elif month == 11:
    monthname = "November"
    days = "30"
elif month == 12:
    monthname = "December"
    days = "31"

# This line of code just prints the different variables to output and tell the user how many days are in the month
# from the year he had inputted. It also outputs the name of the month rather than just the integer associated with it.
print(monthname, year, "has", days + " days")
