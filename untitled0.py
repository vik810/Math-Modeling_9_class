from physconst import g
from math import tan, sin, cos, pi
h=100
B=pi/5
A=pi/3
V=(g*h/tan(B)**2/(2*cos(A)**2*(1-1/tan(B)*tan(A))))**0.5
print(V)