import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
fig, ax = plt.subplots()

dot, = plt.plot([], [], 'o', color='y')

xdata = []
ydata = []

ax.set_ylim(-10, 10)
ax.set_xlim(-10, 50)

R = 10

def cicloid(t): 
    xdata.append(R*np.cos(t)**3)
    ydata.append(R*np.sin(t)**3)
    dot.set_data(xdata, ydata)
    return dot

anim = FuncAnimation(fig, 
                    cicloid,
                    frames=np.arange(0, 8*np.pi, 0.1),
                    interval=50)
anim.save('anim.gif')
