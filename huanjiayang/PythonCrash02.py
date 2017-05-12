'''
Created on 25 Apr 2017

@author: huanjiayang
'''

# DictionaryType
d = {'k1':1,
     'k2':'2',
     3:4}

print d
print d[3]

# Nesting 
d = {'key1' : {'innerKey' : [1,2,3,4]}}
print d['key1']['innerKey'][2]

# Boolean
b = False
print b

#tuple
t = (1,2,3,4)
print t[1]
# different is that you cannot reassign value to tuple element
#you can not do this:
#t[1] = 2


#set
#elements are unique
s = {1,1,1,1,3,5,3,1,32,3}
print s
#set is not ordered/indexed
#you cannot do this:
# print s[2]

for ss in s:
    print ss
    

#Comparision operators    
print 'hi' == 'hi'
print 'a' < 'b'
print 1<2 and 2<1
print 1<2 or 2<1

# with the condition 
if True:
    print 'This is a true'

x=2
if x<2:
    print 'x is less than 2'
elif x==2:
    print "x equals to 2"
else:
    print 'x is not less than 2'