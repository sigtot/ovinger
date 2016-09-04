import math
#h = 10**-3 #pow(10,-3)
#x = 3.14
h = float(input("Gi meg en h "))
x = float(input("Gi meg en x "))
f1 = math.sin(x)
f2 = math.sin(x+h)

print("Deriverte blir",round((f2-f1)/h,4))
print("And some more")