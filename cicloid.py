import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
fig, ax = plt.subplots()

dot, = plt.plot([], [], 'o')

xdata = []
ydata = []

ax.set_ylim(-5, 5)
ax.set_xlim(0, 50)

R = 1

def cicloid(t): 
    xdata.append(R*(t-np.sin(t)))
    ydata.append(R*(1-np.cos(t)))
    dot.set_data(xdata, ydata)
    return dot

ani = FuncAnimation(fig, 
                    cicloid,
                    frames=np.arange(0, 8*np.pi, 0.1),
                    interval=500)
ani.save('ani.gif')
