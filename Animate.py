import UNweightedSAW
import WeightedSAW
import pylab
from matplotlib.animation import FuncAnimation

North = UNweightedSAW.Facing(0) # generate the North facing object
South = UNweightedSAW.Facing(1) # generate the South facing object
East = UNweightedSAW.Facing(2)  # generate the East facing object
West = UNweightedSAW.Facing(3)  # generate the West facing object

def animate(N, fname, weighted):
    ts = [i for i in range(N)]
    sidelength = N*2 + 2
    if weighted:
        w = WeightedSAW(sidelength)
    else:
        w = UNweightedSAW.Walker(sidelength)
    xs = [0]
    ys = [0]

    def init():
        ax.plot([0], [0], ".b", ms = 1)
    
    def update(frame):
        w.step()
        xs.append(w._x)
        ys.append(w._y)
        art = ax.plot(xs, ys, ".b-", ms = 5, lw = 2)
        return art
    
    fig, ax = pylab.subplots()
    ax.set_xlim(-(N//2), N//2)
    ax.set_ylim(-(N//2), N//2)
    ax.set_xticks([i for i in range(-N//2, N//2)])
    ax.set_yticks([i for i in range(-N//2, N//2)])
    ax.grid(True)
    fig.set_facecolor((.992,.945,.969))

    ani = FuncAnimation(fig, update, init_func = init, frames = ts, interval = 400, blit = False, repeat = False)
    ani.save("Figures/Animations/" + fname + ".gif")

if __name__ == "__main__":
    Ns = [n for n in range(10, 30, 5)]
    fiuw = ["N" + str(s) + "-uw" for s in Ns]
    fiw = ["N" + str(s) + "-w" for s in Ns]
    for i in range(len(Ns)):
        animate(Ns[i], fiuw[i], weighted = False)
        animate(Ns[i], fiw[i], weighted = True)