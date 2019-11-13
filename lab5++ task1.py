import matplotlib.pyplot as plt 
def kub(a=1):
    b=a/8**0.5
    plt.plot([1, a+1, a+1, 1, 1], [1, 1, a+1, a+1, 1])
    plt.plot([a+1, a+1+b, a+1+b],[1, 1+b, a+1+b])
    plt.plot([1, 1+b, 1+b+1, a+1], [a+1, a+1+b, a+1+b, a+1])
    plt.plot([1, b+1, a+b+1], [1, b+1, b+1], linestyle='--')
    plt.plot([b+1, b+1], [b+1, a+b+1], linestyle='--', color='r')
    plt.axis('equal')
    plt.show()
kub()