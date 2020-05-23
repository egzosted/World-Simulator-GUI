from Organisms.Plant import Plant
import copy


class Guarana(Plant):
    def __init__(self, x, y, world):
        super(Plant, self).__init__()
        self._name = "Guarana"
        self._symbol = "U"
        self._power = 0
        self._courage = 0
        self._positionX = x
        self._positionY = y
        self._backgroundColor = "magenta2"  # Guarana has white symbol on magenta background
        self._foregroundColor = "white"
        world.isOccupied[self._positionX][self._positionY] = 1

    def collision(self, world, offender):
        new_power = offender.get_power() + 3
        offender.set_power(new_power)
        super(Guarana, self).collision(world, offender)

    def create_clone(self):
        return copy.deepcopy(self)