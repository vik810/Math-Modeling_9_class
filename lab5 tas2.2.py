import matplotlib.pyplot as plt
import numpy as np
def giperbola(a=4, b=2):
    x = np.arange(-10,10,0.01)
    y = (x**2/a**2 - 1)*b**2
    plt.plot(x,y,color='k',label='giperbola')
    plt.xlabel('coord x')
    plt.ylabel('coord y')
    plt.show()
    
giperbola()    