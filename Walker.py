from random import random

class Facing:
        def __init__(self, num):
            self._facingops = ["North", "South", "East", "West"]
            self.cardinal = self._facingops[num]
            self._movelist()
        
        def _movelist(self):
            if self.cardinal == "North":
                self._moves = ["up", "down", "left", "right"]
            elif self.cardinal == "South":
                self._moves ["down", "up", "right", "left"]
            elif self.cardinal == "East":
                self._moves = ["right", "left", "up", "down"]
            elif self.cardinal == "West":
                self._moves = ["left", "right", "down", "up"]

        def convert_movement(self, move_num):
            return self._movelist[move_num]


North = Facing(0)
South = Facing(1)
East = Facing(2)
West = Facing(3)
facing_order = [North, East, South, West]

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
    
    def up(self):
        self._y += 1     # move up a y position in graph
        self._gridy += 1 # move up a y position in GRID
        self.update()    # update the histories
    
    def step(self):
        if self._last is None:
            self.up()
        else:
            rval = int(round((random() * 2) + 1)) # generate random integer 1, 2, or 3
