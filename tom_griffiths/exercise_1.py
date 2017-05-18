'''
Created on 18 May 2017

@author: thomasgriffiths
'''
#===============================================================================
# Question:
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
# 
# Hints: 
# Consider use range(#begin, #end) method
#===============================================================================

# Define numbers and initialise new list
numbers = range(2000,3201)
numbers2 = []

# For each number calculate if it is divisible by 7 while not being a multiple of 5
# Add only these numbers into new list 
for i in numbers:
    if i%7 == 0 and i%5!= 0:
        numbers2.append(str(i))
         
# Print comma separated values from new list
print ', '.join(numbers2)


    