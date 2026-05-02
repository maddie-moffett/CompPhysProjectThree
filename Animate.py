import Walker
import WeightedSAW
import pylab
from matplotlib.animation import FuncAnimation

North = Walker.Facing(0) # generate the North facing object
South = Walker.Facing(1) # generate the South facing object
East = Walker.Facing(2)  # generate the East facing object
West = Walker.Facing(3)  # generate the West facing object

def animate():
    N = 10
    ts = [i for i in range(N)]
    sidelength = 200
    w = WeightedSAW.Walker()
    lastpoint = [0, 0]

    def init():
        pylab.plot([0], [0], ".b", ms = 1)
    
    def update():
        w.step()
        pylab.plot([lastpoint[0], w._x], [lastpoint[1], w._y], ".b-", ms = 1)
        lastpoint = [w._x, w._y]
    
    fig, ax = pylab.subplots()
    ax.set_xlim(-(sidelength//2), sidelength//2)
    ax.set_ylim(-(sidelength//2), sidelength//2)

    ani = FuncAnimation(fig, update, init_func = init, frames = ts, interval = 1, blit = True, repeat = False)