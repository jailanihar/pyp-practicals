import numpy as np
from numpy.lib.arraysetops import isin
import pandas as pd
from pirate import pirate

class map:
    def __init__(self, no_of_rows = 5, no_of_columns = 5):
        self.__arena = np.full([no_of_rows, no_of_columns], None)

    def check_coordinates(self, x, y):
        if x >= 0 and x < self.__arena.shape[0] \
            and y >= 0 and y < self.__arena.shape[1]:
            return True
        return False

    def select_pirate(self, x, y):
        pass

    def check_pirate_name(self, p):
        for x in range(self.__arena.shape[0]):
            for y in range(self.__arena.shape[1]):
                if self.__arena[x][y] != None and \
                    self.__arena[x][y].name == p.name:
                    return True
        return False

    def add_pirate(self, x, y, p):
        if self.check_coordinates(x, y) and \
            isinstance(p, pirate) and not self.check_pirate_name(p):
            self.__arena[x][y] = p

    def move_pirate(self, x, y, new_x, new_y):
        pass

    def __str__(self):
        arena_copy = self.__arena.copy()
        for x in range(arena_copy.shape[0]):
            for y in range(arena_copy.shape[1]):
                if arena_copy[x][y] == None:
                    arena_copy[x][y] = '[]'
        p = pd.DataFrame(arena_copy)
        return str(p)