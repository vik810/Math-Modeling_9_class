def mass_func(M):
    
    """ функцию, которая перемножает все элементы входного массива,
        подающегося на входвкачестве аргумента
    """
    p=1
    for i in range(0, len(M), 1):
        p=p*M[i]
        
    return p
    
     
    
import numpy as np
M=np.arange(1, 10, 1)

print(mass_func(M))