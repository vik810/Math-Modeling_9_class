x0=0
V0x=1
y0=0
V0y=50
import numpy as np
from physconst import g
t=np.arange(0, 5, 0.1)
n=len(t)
print(type(n))
txy = np.ndarray(shape=(n,3))
for i in range(0, n, 1):
    x=x0+V0x*t[i]
    y=y0+V0y*t[i]-g*t[i]**2/2
    txy[i, 0] = t[i]
    txy[i, 1] = x
    txy[i, 2] = y

print(txy)
    