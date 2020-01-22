import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

a=np.pi*30/180
F1= 35
F2= 37
F3= 38
F4= 34
m= 10

t= np.arange(0, 50, 1)

def just_func(z, t):
    x, v_x, y, v_y = z
    dxdt = v_x
    dv_xdt = (F1+ F2*np.cos(a)+ F3*np.sin(a))/m
    dydt = v_y
    dv_ydt = (F2*np.sin(a)+ F3*np.cos(a)+ F4)/m
    return dxdt, dv_xdt, dydt, dv_ydt

x0 = 0
v_x0 = -150
y0 =0 
v_y0 = 5
z0= x0, v_x0, y0, v_y0

sol= odeint(just_func, z0, t)

fig =plt.figure()
smth= []

for i in range(0, len(t), 1):
    telo,= plt.plot(sol[i,0], sol[i,2], 'ro') 
    smth.append([telo])
    
ani= ArtistAnimation(fig, smth, interval=50)
plt.axis('equal')
ani.save('lab.gif')