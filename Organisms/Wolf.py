from Organisms.Animal import Animal
import copy


class Wolf(Animal):
    def __init__(self, x, y, world):
        super(Animal, self).__init__()
        self._name = "Wolf"
        self._symbol = "W"
        self._power = 9
        self._courage = 5
        self._positionX = x
        self._positionY = y
        self._backgroundColor = "gray25"  # wolf has white symbol on gray background
        self._foregroundColor = "white"
        world.isOccupied[self._positionX][self._positionY] = 1

    def create_clone(self):
        return copy.deepcopy(self)
