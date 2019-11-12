import matplotlib.pyplot as plt
import numpy as np
def parabola(a=4, b=2, c=0.5):
    x = np.arange(-10,10,0.01)
    y = a*x**2 + b*x + c
    plt.plot(x,y,color='k',label='papabola')
    plt.xlabel('coord x')
    plt.ylabel('coord y')
    plt.show()
    
parabola()    