In this example a, b, c only exist within the function and are not defined as variables. Variables CAN be defined and used, but in the below example, everything is undefined and will only mutliply integers. 

def function(a, b, c): 
	print a, b, c
	return a*b*c

WILL RETURN: 
In [9]: function(1,2,3)
1 2 3
Out[9]: 6

OR

You can define variables like A B and C and then pass those to the function.

a = 2 
b = 5
c = 8

In [14]: function(a,b,c)
2 5 8
Out[14]: 80

Disclaimer: You do not need to "print" in functions, you just care about the output, the "print" is just for clarity.

