from Organisms.Plant import Plant
import copy


class Grasp(Plant):
    def __init__(self, x, y, world):
        super(Plant, self).__init__()
        self._name = "Grass"
        self._symbol = "G"
        self._power = 0
        self._courage = 0
        self._positionX = x
        self._positionY = y
        self._backgroundColor = "green"  # grasp has white symbol on green background
        self._foregroundColor = "white"
        world.isOccupied[self._positionX][self._positionY] = 1

    def create_clone(self):
        return copy.deepcopy(self)