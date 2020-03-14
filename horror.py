#from sympy import *
#L = Function('L')
#v_f1 = Function('v_f1')
#v_f2 = Function('v_f2')
#phi1 = Function('phi1')
#phi2 = Function('phi2')
#
#
#t = Symbol('t')
#m1 = Symbol('m1')
#m2 = Symbol('m2')
#l1 = Symbol('l1')
#l2 = Symbol('l2')
#g = Symbol('g')
#
#L= ((m1+m2)/2*l1**2*v_f1(t)**2 + m2/2*l2**2*v_f2(t)**2 
#    + m2*l1*l2*v_f1(t)*v_f2(t)*cos(phi1(t)-phi2(t))
#    + (m1+m2)*g*l1*cos(phi2(t)))
#print(diff(L, phi1(t)))
#print(diff(L, phi2(t)))
#print()
#print(diff(diff(L, v_f1(t)),t))
#print(diff(diff(L, v_f2(t)),t))
#
#
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt 
from matplotlib.animation import ArtistAnimation

N =200
t = np.linspace(0, 10, N)

def move_func(s, t):
    phi1, v_f1, phi2, v_f2 = s
    
    dphi1dt = v_f1
    
    dv_f1dt = (2*l1**2*(m1/2 + m2/2)*a1 - l1*l2*m2*(v_f1(t)-v_f2(t))*v_f2(t)*sin(phi1(t) 
    - phi2(t)) + l1*l2*m2*cos(phi1(t) - phi2(t))*Derivative(v_f2(t), t))
    
    dv
    
    return dphi1dt, dv_f1dt, dphi2dt, dv_f2dt


phi0 = np.pi/4
v_f0 = 3

s0 = phi0, v_f0

g =9.8
m = 10
omega = 0.5
l = 1
r = 1

sol = odeint(move_func, s0, t)

x1 = r * np.sin(omega*t[:])
y1 = -r * np.cos(omega*t[:])

x2 = x1 + l * np.sin(sol[:, 0])
y2 = y1 - l * np.cos(sol[:, 0])

fig = plt.figure()
bodys =[]

for i in range(0, len(t), 1):
    thisx = [0, x1[i], x2[i]]
    thisy = [0, y1[i], y2[i]]
    body1, = plt.plot(thisx, thisy, '-', color='r')
    body1_line, = plt.plot(thisx, thisy, 'o', color='r')
    
    bodys.append([body1, body1_line])
    
ani = ArtistAnimation(fig, bodys, interval=50)
plt.axis('equal')
plt.grid()
ani.save('palki.gif')