import matplotlib.pyplot as plt 
def lyns_ray_parall_main_os(F=10, vid='собирающая'):
    plt.plot([25, 25], [5, 1], color='k', marker='^')
    plt.plot([1, 50], [3, 3])
    plt.plot([1, 25], [4, 4], color='k', marker='>')
    if vid=='собирающая':
        plt.plot([25, 25+F], [4, 3], color='k', marker='v')
    if vid=='рассеиващая': 
        
    plt.show()
    
lyns_ray_parall_main_os()