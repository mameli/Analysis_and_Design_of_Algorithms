from sympy import *
from sympy.abc import x, y
from sympy import Symbol, factorial

frac = 2.0/4
print frac, type(frac)

frac = 2//4
print frac, type(frac)

frac = Integer(2)/4
print type(frac)

print frac

print S(1)/3 + S(4)/5 - Integer(7)/6

print factorial(3)
