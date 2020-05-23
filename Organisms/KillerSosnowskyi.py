from Organisms.Plant import Plant
import copy


class KillerSosnowskyi(Plant):
    def __init__(self, x, y, world):
        super(Plant, self).__init__()
        self._name = "KillerSosnowskyi"
        self._symbol = "K"
        self._power = 0
        self._courage = 0
        self._positionX = x
        self._positionY = y
        self._backgroundColor = "red"  # killer has white symbol on red background
        self._foregroundColor = "white"
        world.isOccupied[self._positionX][self._positionY] = 1

    def action(self, world):
        self.kill(world, self.get_x(), self.get_y() - 1)  # kill left enemy
        self.kill(world, self.get_x(), self.get_y() + 1)  # kill right enemy
        self.kill(world, self.get_x() - 1 , self.get_y())  # kill up enemy
        self.kill(world, self.get_x() + 1, self.get_y())  # kill down enemy
        super(KillerSosnowskyi, self).action(world)

    def kill(self, world, x, y):
        o = None
        if self.is_inside(x, y, world.get_height(), world.get_width()):
            for i in world.organisms:
                if i.get_x() == x and i.get_y() == y and i.deleteMe == 0:
                    o = i
                    break
            if o is not None and o.get_courage() > 0 and o.get_name() != "CyberSheep":
                world.isOccupied[x][y] = 0
                world.report += o.get_name()
                world.report += " poisoned by "
                world.report += self.get_name()
                world.report += "\n"
                if o.get_name() == "Human":
                    world.mark_end()
                o.deleteMe = 1

    def collision(self, world, offender):
        if offender.get_name() != "CyberSheep":
            self.poisoning_collision(world, offender)
        else:
            super(KillerSosnowskyi, self).collision(world, offender)

    def create_clone(self):
        return copy.deepcopy(self)