'''
Created on 25 Apr 2017

@author: huanjiayang
'''
x = 1

print "1/2 = " + str(1 / 2)
print "1/2.0 = " + str(1 / 2.0)
print "1.0/2 = " + str(1.0 / 2)

x=2
print x

x=x+x
print x

# This is a Comment
print "I'm Huanjia"
print 'I want a double quote like this "'

print "I've just set x to {}".format(x)

y = 3
print "actually x is now {xxx}, y is now {yyy}".format(yyy=y,xxx=x)

#String indexing
s = "this is a string"
print s[5]

#Slice Notation, start index is included, end index is not included
print s[:8]
print s[5:]
print s[5:8]

#list
myList = [1,2,3,'as'] #Note this is very bad practice
print myList[3]
print myList[:2]

myList.append('what')
print myList
myList[2] = 'ah'
print myList

#Nested list
nestList = [1,2,3,[1,2,3,['what the']]]
print nestList[3][3][0]