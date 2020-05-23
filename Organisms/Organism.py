from abc import ABC, abstractmethod


class Organism(ABC, object):
    def __init__(self):
        self._name = ""
        self._symbol = ""
        self._power = None
        self._courage = None
        self._backgroundColor = ""
        self._foregroundColor = ""
        self._positionX = None
        self._positionY = None
        self._adulthood = True     # flag to define if organism is enough old to move
        self._LEFT = 0  # variables defining direction
        self._RIGHT = 1
        self._UP = 2
        self._DOWN = 3
        self.deleteMe = 0

    @staticmethod
    def is_inside(x, y, height, width):
        if x < 0 or y < 0 or x >= height or y >= width:
            return 0
        return 1

    def did_die(self, offender):
        if self._power <= offender.get_power():
            return 1
        return 0

    @staticmethod
    def is_empty(x, y, world):
        if y - 1 >= 0 and world.isOccupied[x][y - 1] == 0:  # first we check reproduction on left side
            world.set_coordinates(x, y - 1)
            return True
        if y + 1 < world.get_width() and world.isOccupied[x][y + 1] == 0: # check reproduction on right side
            world.set_coordinates(x, y + 1)
            return True
        if x - 1 >= 0 and world.isOccupied[x - 1][y] == 0:  # check reproduction on top side
            world.set_coordinates(x - 1, y)
            return True
        if x + 1 < world.get_height() and world.isOccupied[x + 1][y] == 0:  # check reproduction on bottom side
            world.set_coordinates(x + 1, y)
            return True
        return False

    def get_name(self):
        return self._name

    def get_symbol(self):
        return self._symbol

    def get_power(self):
        return self._power

    def get_courage(self):
        return self._courage

    def get_x(self):
        return self._positionX

    def get_y(self):
        return self._positionY

    def get_adulthood(self):
        return self._adulthood

    def get_background_color(self):
        return self._backgroundColor

    def get_foreground_color(self):
        return self._foregroundColor

    def set_x(self, x):
        self._positionX = x

    def set_y(self, y):
        self._positionY = y

    def set_power(self, power):
        self._power = power

    def set_adulthood(self, adulthood):
        self._adulthood = adulthood

    @abstractmethod
    def action(self, world):
        pass

    @abstractmethod
    def collision(self, world, offender):
        pass

    @abstractmethod
    def create_clone(self):
        pass
