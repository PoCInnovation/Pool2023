import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import re

def get_dataset(batch_size = 100, noise = 0.1):
    x = np.linspace(0, 100, batch_size)
    f = lambda x: (2/3) * x - 3
    noise = np.random.normal(0, noise, x.shape)
    y = f(x) + noise
    
    return x, y

def display_dataset(x, y, neuron = None):
    fig = plt.figure()
    ax = plt.axes()
    
    if not neuron == None:
        ax.plot(x, neuron.w * x + neuron.b, 'r--', zorder=5)
    ax.scatter(x, y, zorder=10)
    ax.grid()
    ax.set_title('Representation of the dataset')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    plt.axhline(0, color='black', zorder=0)
    plt.axvline(0, color='black', zorder=0)
    plt.show()

def display_function(x, f):
    fig = plt.figure()
    ax = plt.axes()

    ax.plot(x, f(x))
    ax.grid()
    ax.set_title('Representation of the ' + f.__name__ + ' function')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    plt.show()
    
def display_loss_history(loss, epochs):
    fig = plt.figure()
    ax = plt.axes()
    
    ax.plot(np.linspace(0, epochs, epochs), loss)
    ax.grid()
    ax.set_title('Evolution of loss over epochs')
    ax.set_xlabel('epoch')
    ax.set_ylabel('loss')
    plt.show()
    
def start_board_computer(neuron):
    power = -1

    while power < 0 or power > 100:
        power = input('Engine power required (0% - 100%): ')
        if re.search(r'^\d{1,3}%$', power):
            power = int(power[0:-1])
            power = power if power <= 100 else -1
        else:
            power = -1

    print('--- BOARD COMPUTER ---')
    print('Initial engine power: %d%%' % power)
    print('Maximum planned altitude: %dkm' % neuron.forward(power))
