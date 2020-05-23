from abc import ABC, abstractmethod
from Organisms.Organism import Organism
import random


class Animal(Organism, ABC):
    def __init__(self):
        super(Animal, self).__init__(self)
        self._nextX = None
        self._nextY = None

    def action(self, world):
        direction = 0
        found = 0
        while found == 0:
            direction = random.randint(0, 3)
            found = self.is_movement_inside(world, direction)
        self.set_next_xy(direction)
        self.move(world)

    def reproduce(self, world):
        if self.is_empty(self.get_x(), self.get_y(), world):
            world.report += self.get_name()
            world.report += " has been born\n"
            o = self.create_clone()
            o.setAdulthood = False
            o.set_x(world.get_first_coordinate())
            o.set_y(world.get_second_coordinate())
            world.add_organism(o)
            world.isOccupied[o.get_x()][o.get_y()] = 1

    def move(self, world):
        if world.isOccupied[self._nextX][self._nextY] == 0:
            world.isOccupied[self._positionX][self._positionY] = 0
            self._positionX = self._nextX
            self._positionY = self._nextY
            world.isOccupied[self._nextX][self._nextY] = 1
        else:
            for i in range(world.get_size_organisms()):
                if world.organisms[i].get_x() == self._nextX and world.organisms[i].get_y() == self._nextY and world.organisms[i].deleteMe == 0:
                    defender = world.organisms[i]
                    defender.collision(world, self)
                    break

    def is_movement_inside(self, world, direction):
        found = 0
        if direction == self._LEFT:
            found = self.is_inside(self._positionX, self._positionY - 1, world.get_height(), world.get_width())
        elif direction == self._RIGHT:
            found = self.is_inside(self._positionX, self._positionY + 1, world.get_height(), world.get_width())
        elif direction == self._UP:
            found = self.is_inside(self._positionX - 1, self._positionY, world.get_height(), world.get_width())
        else:
            found = self.is_inside(self._positionX + 1, self._positionY, world.get_height(), world.get_width())
        return found

    def set_next_xy(self, direction):
        if direction == self._LEFT:
            self._nextY = self._positionY - 1
            self._nextX = self._positionX
        elif direction == self._RIGHT:
            self._nextY = self._positionY + 1
            self._nextX = self._positionX
        elif direction == self._UP:
            self._nextY = self._positionY
            self._nextX = self._positionX - 1
        else:
            self._nextY = self._positionY
            self._nextX = self._positionX + 1

    def collision(self, world, offender):
        is_dead = self.did_die(offender)
        if is_dead == 0:
            self.defender_won(world, offender)
        elif self.get_name() == offender.get_name():
            self.reproduce(world)
            self.set_adulthood(False)
        else:
            self.offender_won(world, offender)

    def defender_won(self, world, offender):
        world.isOccupied[offender.get_x()][offender.get_y()] = 0
        if offender.get_name() == "Human":
            world.mark_end()
        world.report += offender.get_name()
        world.report += " killed by "
        world.report += self._name
        world.report += "\n"
        offender.deleteMe = 1

    def offender_won(self, world, offender):
        world.isOccupied[offender.get_x()][offender.get_y()] = 0
        if self.get_name() == "Human":
            world.mark_end()
        world.report += self.get_name()
        world.report += " killed by "
        world.report += offender.get_name()
        world.report += "\n"
        self.deleteMe = 1
        offender.set_x(self.get_x())
        offender.set_y(self.get_y())

    @abstractmethod
    def create_clone(self):
        pass
