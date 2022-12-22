import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

def display_function(x, f):
    fig = plt.figure()
    ax = plt.axes()

    ax.plot(x, f(x))
    ax.grid()
    ax.set_title('Representation of the ' + f.__name__ + ' function')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    plt.show()
    
    
def display_functions(x, f, g, f_dx = None, g_dx = None):
    fig = plt.figure()
    gs = GridSpec(1, 2, figure=fig)
    
    ax_f = fig.add_subplot(gs[0, 0])
    ax_g = fig.add_subplot(gs[0, 1])
    
    if not f_dx == None:
        ax_f.plot(x, f_dx(x), zorder=1)
    ax_f.plot(x, f(x), zorder=0)
    ax_f.grid(zorder=-1)
    ax_f.set_title('Representation of the ' + f.__name__ + ' function')
    ax_f.set_xlabel('x')
    ax_f.set_ylabel('y')
    
    if not g_dx == None:
        ax_g.plot(x, g_dx(x), zorder=1)
    ax_g.plot(x, g(x), zorder=0)
    ax_g.grid(zorder=-1)
    ax_g.set_title('Representation of the ' + g.__name__ + ' function')
    ax_g.set_xlabel('x')
    ax_g.set_ylabel('y')
    
    plt.show()
    
    
def gradient_descent_visualisation(x, f, min):
    #min = steps[-1]
    fig = plt.figure()
    
    ax = plt.axes()
    ax.grid(zorder=0)
    ax.plot(x, f(x), '--', zorder=1)
    #ax.scatter(steps, f(steps), c='red', s=10, zorder=2)
    ax.scatter(x, f(x), c='red', s=10, zorder=3)
    ax.scatter(min, f(min), c='green', s=20, zorder=3)
    ax.set_title('Gradient descent on ' + f.__name__)
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
    