from Neuron import Neuron
from random import randint
import time
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation




fig, ax = plt.subplots()
fig.set_tight_layout(True)

# Query the figure's on-screen size and DPI. Note that when saving the figure to
# a file, we need to provide a DPI for that separately.
print('fig size: {0} DPI, size in inches {1}'.format(
    fig.get_dpi(), fig.get_size_inches()))

# Plot a scatter that persists (isn't redrawn) and the initial line.
x = np.arange(0, 20, 0.1)

def update(i):
    ax.scatter(i, neuron.get_voltage(), s=None, c=220)
    if neuron.is_resting:
        if randint(0, 3) == 1:
            neuron.react(randint(4, 17))
    neuron.notice()
    neuron.interact()
    neuron.notice()
    time.sleep(0.5)
    return ax

if __name__ == '__main__':
    neuron = Neuron("Steven", 10, 10)
    neuron.notice()
    # stimulus = randint(10, 17)
    # print "Stimulus {}".format(stimulus)
    anim = FuncAnimation(fig, update, frames=np.arange(0, 100, 0.1), interval=1)
    if len(sys.argv) > 1 and sys.argv[1] == 'save':
        anim.save('line.gif', dpi=80, writer='imagemagick')
    else:
        # plt.show() will just loop the animation forever.
        plt.show()
