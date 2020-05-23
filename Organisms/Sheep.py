from Organisms.Animal import Animal
import copy


class Sheep(Animal):
    def __init__(self, x, y, world):
        super(Animal, self).__init__()
        self._name = "Sheep"
        self._symbol = "S"
        self._power = 4
        self._courage = 4
        self._positionX = x
        self._positionY = y
        self._backgroundColor = "white"  # sheep has black symbol on white background
        self._foregroundColor = "black"
        world.isOccupied[self._positionX][self._positionY] = 1

    def create_clone(self):
        return copy.deepcopy(self)