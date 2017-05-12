'''
Created on 25 Apr 2017

@author: huanjiayang
'''

#Map
def calSquare(num):
    return num**2


s = [1,2,3,4,5,6,7,8,9]

myList = map(calSquare,s)
print myList


#Lambda Expression -- anonymous function
yourList = map(lambda num:num**0.5, myList)
print yourList


#Filter
theirList = filter(lambda num:num%2==0,myList)
print theirList



s = "What the"
s.lower()
print s
print s.split()
print s.split('t')



#Tuple and packing
x = [(1,2),(3,4),(5,6)]

for item in x:
    print item

for (a,b) in x:
    print "This is a: {}, This is b:{}".format(a,b)