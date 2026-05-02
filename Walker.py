from random import random

class Facing:
        def __init__(self, num):
            self._facingops = ["North", "South", "East", "West"]
            self.cardinal = self._facingops[num]
            self._movelist()
        
        def _movelist(self):
            if self.cardinal == "North":
                self._moves = ["left", "up", "right", "down"]
            elif self.cardinal == "South":
                self._moves ["right", "down", "left", "up"]
            elif self.cardinal == "East":
                self._moves = ["up", "right", "down", "left"]
            elif self.cardinal == "West":
                self._moves = ["down", "left", "up", "right"]

        def convert_movement(self, move_num):
            return self._movelist[move_num]
        
        def __str__(self):
            return self.cardinal


North = Facing(0)
South = Facing(1)
East = Facing(2)
West = Facing(3)

class Walker:
    
    def __init__(self, sidelength = 100):
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

    def _make_grid(self, sidelength):
        g = [li for li in [False for _ in range(sidelength)]] # make 2D grid full of False (has not been there) with sidelengths provided
        g[self._gridx][self._gridy] = True                    # current occupied position has been occupied
        return g                                              # return the grid 
    
    def update(self):
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
        if objectivemove == "up":
            self._up()
            self._last = "up"
        elif objectivemove == "down":
            self._down()
            self._last = "down"
        elif objectivemove == "left":
            self._left()
            self._last = "left"
        elif objectivemove == "right":
            self._right()
            self._last = "right"
    
    def _up(self):
        self._y += 1     # move up a y position in graph
        self._gridy += 1 # move up a y position in GRID
        self.update()    # update the histories
    
    def _down(self):
        self._y -= 1     # move down a y position in graph
        self._gridy -= 1 # move down a y position in GRID
        self.update()    # update the histories
    
    def _left(self):
        self._x -= 1     # move down an x position in graph
        self._gridx -= 1 # move down an x position in GRID
        self.update()    # update the histories
    
    def _right(self):
        self._x += 1     # move up an x position in graph
        self._gridx += 1 # move up an x position in GRID
        self.update()    # update the histories
    
    def _spin(self, relativemove):
        self._facing = self._spinlist[relativemove]
        if self._facing == North:
            self._spinlist = [West, North, East, South]
        elif self._facing == South:
            self._spinlist = [East, South, West, North]
        elif self._facing == East:
            self._spinlist = [North, East, South, West]
        elif self._facing == West:
            self._spinlist = [South, West, North, East]
    
    def step(self):
        if self._last is None:
            self.up()
        else:
            rval = int(round((random() * 2) + 1))               # generate random integer 1, 2, or 3
            relativemove = ["left", "up", "right"][rval]        # convert to the move relative to the walker's facing
            objectivemove = self._facing.convert_movement(rval) # convert the relative move to an objective move through the plot
            if self.check(objectivemove):                       # if have visited the proposed spot before, terminate
                self.terminate()
            else:                                               # else take the step
                self._move(objectivemove)                       # move location
                self._spin(relativemove)                        # change direction facing


    def terminate(self):
        return Walker()