#!/usr/bin/env python
#below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
end=1000
value=1
factors=[]
while value<end:
	if(not value%3 or not value%5):factors.append(value)
	value+=1
print(sum(factors), factors)


