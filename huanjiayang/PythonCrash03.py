'''
Created on 25 Apr 2017

@author: huanjiayang
'''

seq = [1,2,3,4,5,6,7,8,9]

for i in seq:
    print '{x} * {x} is {y}'.format(y=i*i,x=i)
    
    
i = 0
while i<6:
    print i
    i=i+1
    
    
    
#Range function
print range(0,4) 

myList = range(0,9)
print myList

for i in range(0,9):
    print i
    

# List comprehension
out = []
for num in myList:
    out.append(num**2)

print out
#This is the same to 
print [num**2 for num in myList]


# function
def myFunction(p1,p2):
    print 'This is p1: {}, this is p2: {}'.format(p1,p2)
    

myFunction(1,2)

#default parameter value
def myDefaultFunction(p = 3):
    print 'this is p: {}'.format(p)
    
myDefaultFunction()
myDefaultFunction(5)

#returning value in function
def calSquare(n):
    """
     This is multi-line comments, this is called here the documentation string
    """
    return n**2

print calSquare(56)