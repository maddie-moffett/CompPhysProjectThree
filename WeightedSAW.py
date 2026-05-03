from random import random
from numpy import mean
import pylab

class Facing:
        def __init__(self, num):
            facingops = ["North", "South", "East", "West"]    # options for the facing directions
            self.cardinal = facingops[num]                    # the cardinal direction of this facing based on index provided
            self._makemovelist()                              # generate the moves list
        
        def _makemovelist(self):                               # assign the objective direction of movement based on relative movement and facing direc
            if self.cardinal == "North":
                self._movelist = ["left", "up", "right", "down"]
            elif self.cardinal == "South":
                self._movelist = ["right", "down", "left", "up"]
            elif self.cardinal == "East":
                self._movelist = ["up", "right", "down", "left"]
            elif self.cardinal == "West":
                self._movelist = ["down", "left", "up", "right"]

        def convert_movement(self, move_num):                 # convert the relative movement given to objective and return
            return self._movelist[move_num]


North = Facing(0) # generate the North facing object
South = Facing(1) # generate the South facing object
East = Facing(2)  # generate the East facing object
West = Facing(3)  # generate the West facing object

class Walker:
    
    def __init__(self, sidelength):
        self.xhist = [0]                                 # history of x values
        self.yhist = [0]                                 # history of y values
        self._x = 0                                      # current x position (in a graphing sense)
        self._y = 0                                      # current y position (in a graphing sense)

        self._gridx = sidelength // 2                    # current x position in a GRID sense
        self._gridy = sidelength // 2                    # current y position in a GRID sense
        self._grid = self._make_grid(sidelength)         # make the grid of possible positions

        self._facing = North                             # direction currently facing
        self._last = None                                # Previous step
        self._movelist = ["up", "down", "left", "right"] # order of movements
        self._spinlist = [West, North, East, South]      # order of ways to face

        self._weight = 1                                # array of the weights at each step

    def _make_grid(self, sidelength):
        g = [[False for _ in range(sidelength)] for _ in range(sidelength)] # make 2D grid full of False (has not been there) with sidelengths provided
        g[self._gridx][self._gridy] = True                                  # current occupied position has been occupied
        return g                                                            # return the grid 
    
    def update(self, move):
        self.xhist.append(self._x)                  # append current x val to the history list
        self.yhist.append(self._y)                  # append current y val to the history list
        self._grid[self._gridx][self._gridy] = True # current position in grid is occupied
    
    def num_steps(self):
        return len(self.xhist) - 1 # number of steps is how many x positions we've occupied, minus the first one
    
    def check(self, move):
        if move == "up":
            return self._grid[self._gridx][self._gridy + 1]
        elif move == "down":
            return self._grid[self._gridx][self._gridy - 1]
        elif move == "left":
            return self._grid[self._gridx - 1][self._gridy]
        elif move == "right":
            return self._grid[self._gridx + 1][self._gridy]
    
    def _move(self, objectivemove):     # helper function to ensure call of correct movement
        self._last = objectivemove      # and update last movement
        if objectivemove == "up":
            self._up()
        elif objectivemove == "down":
            self._down()
        elif objectivemove == "left":
            self._left()
        elif objectivemove == "right":
            self._right()
    
    def _up(self):
        self._y += 1         # move up a y position in graph
        self._gridy += 1     # move up a y position in GRID
        self.update("up")    # update the histories
    
    def _down(self):
        self._y -= 1         # move down a y position in graph
        self._gridy -= 1     # move down a y position in GRID
        self.update("down")  # update the histories
    
    def _left(self):
        self._x -= 1         # move down an x position in graph
        self._gridx -= 1     # move down an x position in GRID
        self.update("left")  # update the histories
    
    def _right(self):
        self._x += 1         # move up an x position in graph
        self._gridx += 1     # move up an x position in GRID
        self.update("right") # update the histories
    
    def _spin(self, relativemove):
        self._facing = self._spinlist[relativemove]     # spin to face the new direction depending on facing and relative movement
        if self._facing == North:
            self._spinlist = [West, North, East, South] # also update the spinlist for new facing direction correlating relative move
        elif self._facing == South:                     # to what the new facing would be
            self._spinlist = [East, South, West, North]
        elif self._facing == East:
            self._spinlist = [North, East, South, West]
        elif self._facing == West:
            self._spinlist = [South, West, North, East]
    
    def _availablesteps(self):
        avimoves = []                  # available
        for possi in range(len(self._movelist)):
            if not self.check(self._facing.convert_movement(possi)):
                avimoves.append(possi)
        weight = ((len(avimoves)) / 3)
        self._weight *= weight
        return avimoves
    
    def step(self):
        if self._last is None:                                  # first step is up
            self._move("up")
            return True
        else:
            avimoves = self._availablesteps()                   # weighted adjustment
            if len(avimoves) == 0:
                return False
            rval = int((random() * len(avimoves)) // 1)         # generate random integer 1, 2, or 3
            nval = avimoves[rval]
            objectivemove = self._facing.convert_movement(nval) # convert the relative move to an objective move through the plot                                              # else take the step
            self._move(objectivemove)                           # move location
            self._spin(rval)                                    # change direction facing
            return True
    
    def _r2(self):                       # return r^2 at current position
        return (self._x**2 + self._y**2)
    
    def get_r2_numer(self):              # return the numerator to calculate msr for this walker position (weight * r^2)
        return self._weight*self._r2()
    
    def get_weight(self):                # return weight
        return self._weight


def SAW(N = 25, numwalkers = 1000, sidelength = 50):
    walkers = []           # array to store the walker objects
    numer = 0              # record numerator sum
    denomer = 0            # record denominator sum

    for i in range(numwalkers):                  # iterate through number of walkers
        w = Walker(sidelength)                   # initialize walker
        walking = w.step()                       # take the initial step upwards
        while w.num_steps() <= N and walking:    # while not desired N and don't double back
            walking = w.step()                   # attempt a step
        walkers.append(w)                        # append the current walker object
        numer += w.get_r2_numer()                # sum up the numerator weight and r^2
        denomer += w.get_weight()                # sum up the weights for the denominator
    
    meansquaredr = numer/denomer                 # calculate mean squared r
    return meansquaredr, walkers                 # return meansquared r and walker objects

def FindWeightedMeanR2():
    Nvals = [4, 8, 16, 32]                           # N vals to be tested
    msrs = []                                        # empty array to store the mean squared r vals

    for N in Nvals:                                  # iterate through the n vals we're testing
        msr, _ = SAW(N = N, sidelength = 70)         # calculate SAW
        msrs.append(msr)                             # store it
    
    pylab.plot(Nvals, msrs)                          # plot, label, and show
    pylab.title("Mean Squared R as a Function of N")
    pylab.xlabel("N value")
    pylab.ylabel("Mean Squared R")
    pylab.show()