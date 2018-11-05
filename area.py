#!/usr/bin/env python

def anonymous(x): return x**2 + 1
def integrate(fun, start, end):
	step = .01
	intercept = start
	area = 0
	while intercept < end:
		intercept += step
		height=anonymous(intercept)
		area+=height*step
	return area
print(integrate(anonymous, 0, 10))
#Multiples of 3 and 5.  If we list all the natural numbers below 10 that are multi
