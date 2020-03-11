#import numpy as np
#from sympy import *
#L = Function('L')
#v_f = Function('v_f')
#phi = Function('phi')
#
#t = Symbol('t')
#m = Symbol('m')
#l = Symbol('l')
#r = Symbol('r')
#omega = Symbol('omega')
#g = Symbol('g')
#
#
#
#k1 = m*l**2/2
#k2 = m*r*l*omega**2
#k3 = m*g*l
#L= k1*v_f(t)**2 + k2*cos(phi(t) - omega*t) + k3*cos(phi(t))
#
#print(diff(L, phi(t)))
#print()
#print(diff(diff(L, v_f(t)),t))
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt 
from matplotlib.animation import ArtistAnimation

N =200
t = np.linspace(0, 10, N)

def move_func(s, t):
    phi, v_f = s
    dphidt = v_f
    dv_fdt = (-m*g*l*np.sin(phi)+ m*l*omega**2*r*np.sin(omega*t-phi))/(m*l**2)
    return dphidt, dv_fdt

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