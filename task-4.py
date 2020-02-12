import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt 
from matplotlib.animation import ArtistAnimation

 
def generator_func(r, n, v, x0, y0):
    
    for i in (0, n, 1):
        alpha = 2*np.pi*i/n
        
        if alpha <= np.pi/2:
            x= x0 + r*np.cos(alpha)
            y= y0 + r*np.sin(alpha)
           
            x_v = x + v*np.sin(alpha)
            y_v = y - v*np.cos(alpha)
           
        elif alpha <= np.pi and alpha > np.pi/2:
            x= x0 - r*np.cos(alpha)
            y= y0 + r*np.sin(alpha)
           
            x_v = x + v*np.sin(alpha)
            y_v = y + v*np.cos(alpha)
           
        elif alpha <= 1.5*np.pi and alpha > np.pi:
            x= x0 - r*np.cos(alpha)
            y= y0 - r*np.sin(alpha)
           
            x_v = x - v*np.sin(alpha)
            y_v = y + v*np.cos(alpha)
           
        elif alpha <= 2*np.pi and alpha > 1.5*np.pi:
            x= x0 + r*np.cos(alpha)
            y= y0 - r*np.sin(alpha)
           
            x_v = x - v*np.sin(alpha)
            y_v = y - v*np.cos(alpha)
           
    plt.plot(x, y)
    plt.plot(x_v, y_v)

           
       
    
generator_func(5, 10, 1, 0, 0)
    


         
         
