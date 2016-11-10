#!/bin/python

for x in range(100):
    if x % 3.0 == 0 and x % 5.0 == 0:
    	c = ("%(x)s: fizzbuzz" % locals())
    	print c
    elif x % 3.0 == 0: 
        a = ("%(x)s: fizz" % locals())
        print a
    elif x % 5.0 == 0:
    	b = ("%(x)s: buzz" % locals())
    	print b
    else: 
    	print ""
