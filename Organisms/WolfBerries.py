from Organisms.Plant import Plant
import copy


class WolfBerries(Plant):
    def __init__(self, x, y, world):
        super(Plant, self).__init__()
        self._name = "WolfBerries"
        self._symbol = "B"
        self._power = 0
        self._courage = 0
        self._positionX = x
        self._positionY = y
        self._backgroundColor = "pink"  # WolfBerries have white symbol on pink background
        self._foregroundColor = "white"
        world.isOccupied[self._positionX][self._positionY] = 1

    def collision(self, world, offender):
        self.poisoning_collision(world, offender)

    def create_clone(self):
        return copy.deepcopy(self)