# -*- coding: utf8 -*-
import math
def a(h):
	return h*3/math.sqrt(6)

def area(h):
	return math.sqrt(3)*math.pow(a(h),2)

def volume(h):
	return math.pow(a(h),3)*math.sqrt(2)/12
myHeight = int(input("Hva er høyden på tetraeden? "))
print("Overflateareal:",area(myHeight))
print("Volum:",volume(myHeight))