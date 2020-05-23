from Organisms.Plant import Plant
import copy
import random


class Yellow(Plant):
    def __init__(self, x, y, world):
        super(Plant, self).__init__()
        self._name = "Yellow"
        self._symbol = "Y"
        self._power = 0
        self._courage = 0
        self._positionX = x
        self._positionY = y
        self._backgroundColor = "yellow"  # yellow is yellow, obvious
        self._foregroundColor = "white"
        world.isOccupied[self._positionX][self._positionY] = 1

    def action(self, world):
        for i in range(3):
            reproduction = random.randint(1, 100)
            if reproduction <= 5:
                self.try_reproduce(world)
                break

    def create_clone(self):
        return copy.deepcopy(self)