# File: Payroll.py
# Student: Cesar Gabriel Ayala-Mendoza
# UT EID: cga773
# Course Name: CS303E
#
# Date: 2/11/2022
# Description of Program: This program takes the input from the user to print/output a payroll statement that has been
# formatted to display money signs ($), percentage signs (%), and a certain number of decimal places for each kind of
# value.

# This section of code takes the input from the user when asked to enter information that is needed to compute the
# amounts for the payroll. The user's input is stored as a variable so mathematical equations cane be performed later.
empName = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked in a week: "))
payRate = float(input("Enter hourly pay rate: "))
fedTaxRate = float(input("Enter federal tax withholding rate: "))
stateTaxRate = float(input("Enter state tax withholding rate: "))

# A new set of variables is created after using the first set of variables to compute the actual amounts that will be
# displayed on the payroll. These new variables have stored values gained from the mathematical equations.
grossPay = hours * payRate
fedHolding = grossPay * fedTaxRate
stateHolding = grossPay * stateTaxRate
totalDeduction = fedHolding + stateHolding
netPay = grossPay - totalDeduction

# This section of the code prints/outputs the payroll and its amounts and uses the format function to make the money
# amounts have two decimal places and the non-money amounts have one decimal place.
print()
print("Employee Name:", empName)
print("Hours Worked:", format(hours, ".1f"))
print("Pay Rate: $", format(payRate, ".2f"), sep="")
print("Gross Pay: $", format(grossPay, ",.2f"), sep="")
print("Deductions:")
print("  Federal Withholding (", format(fedTaxRate, ".1%"), "): $", format(fedHolding, ".2f"), sep="")
print("  State Withholding (", format(stateTaxRate, ".1%"), "): $", format(stateHolding, ".2f"), sep="")
print("  Total Deduction: $", format(totalDeduction, ".2f"), sep="")
print("Net Pay: $", format(netPay, ".2f"), sep="")
