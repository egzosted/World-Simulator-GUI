from Organisms.Animal import Animal
import copy


class CyberSheep(Animal):
    def __init__(self, x, y, world):
        super(Animal, self).__init__()
        self._name = "CyberSheep"
        self._symbol = "C"
        self._power = 11
        self._courage = 4
        self._positionX = x
        self._positionY = y
        self._backgroundColor = "DarkOrchid4"
        self._foregroundColor = "white"
        world.isOccupied[self._positionX][self._positionY] = 1

    def action(self, world):
        direction = 0
        closestKiller = None
        distance_to_killer = 2 * world.get_height() + 2 * world.get_width()
        for i in world.organisms:
            if i.get_name() == "KillerSosnowskyi" and i.deleteMe == 0:
                distance = abs(self.get_x() - i.get_x()) + abs(self.get_y() - i.get_y())
                if distance < distance_to_killer:
                    closestKiller = i
                    distance_to_killer = distance
        if closestKiller is None:
            super(CyberSheep, self).action(world)
        else:
            if self.get_x() != closestKiller.get_x():
                if self.get_x() > closestKiller.get_x():
                    direction = self._UP
                else:
                    direction = self._DOWN
            else:
                if self.get_y() > closestKiller.get_y():
                    direction = self._LEFT
                else:
                    direction = self._RIGHT
            self.set_next_xy(direction)
            self.move(world)

    def create_clone(self):
        return copy.deepcopy(self)