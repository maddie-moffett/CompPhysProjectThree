import UNweightedSAW
import WeightedSAW
import pylab
from matplotlib.animation import FuncAnimation

North = UNweightedSAW.Facing(0) # generate the North facing object
South = UNweightedSAW.Facing(1) # generate the South facing object
East = UNweightedSAW.Facing(2)  # generate the East facing object
West = UNweightedSAW.Facing(3)  # generate the West facing object

def animate(N, fname, weighted):
    ts = [i for i in range(N)]               # frames
    sidelength = N*2 + 2                     # sidelength for walker grid
    if weighted:                             # form walker object weighted or unweighted
        w = WeightedSAW.Walker(sidelength)
    else:
        w = UNweightedSAW.Walker(sidelength)
    xs = [0]                                 # save positional value arrays
    ys = [0]

    def init():                              # init function for animation
        ax.plot([0], [0], ".b", ms = 1)      # starting point
    
    def update(frame):                       # update at each frame
        w.step()                             # take a step
        xs.append(w._x)                      # save the x and y vals
        ys.append(w._y)                      # then plot all of the steps:
        art = ax.plot(xs, ys, ".b-", ms = 5, lw = 2)
        return art
    
    fig, ax = pylab.subplots()               # initialize plot
    ax.set_xlim(-(N//2), N//2)               # bounds of graph
    ax.set_ylim(-(N//2), N//2)               # gridlines:
    ax.set_xticks([i for i in range(-N//2, N//2)])
    ax.set_yticks([i for i in range(-N//2, N//2)])
    ax.grid(True)
    fig.set_facecolor((.992,.945,.969))      # pale pink background for slay

    ani = FuncAnimation(fig, update, init_func = init, frames = ts, interval = 400, blit = False, repeat = False) # animation call!
    ani.save("Figures/Animations/" + fname + ".gif") # save using given filename center

if __name__ == "__main__":
    Ns = [n for n in range(10, 30, 5)]               # N vals we're graphing
    fiuw = ["N" + str(s) + "-uw" for s in Ns]        # file names for unweighted
    fiw = ["N" + str(s) + "-w" for s in Ns]          # file names for weighted
    for i in range(len(Ns)):                         # iterate through
        animate(Ns[i], fiuw[i], weighted = False)    # animate unweighted version at this N
        animate(Ns[i], fiw[i], weighted = True)      # animate weighted version at this N