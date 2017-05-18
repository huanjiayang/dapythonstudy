'''
Created on 18 May 2017

@author: thomasgriffiths
'''

#===============================================================================
# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')
# 
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# tuple() method can convert list to tuple
#===============================================================================

# Define numbers from comma-separated console input
numbers = raw_input("Please enter a comma-separated list of numbers: ")

# Strip numbers from input and convert to list
numlist = numbers.split(",")

# Convert list to tuple
numtuple = tuple(numlist)

# Print list and tuple
print numlist
print numtuple