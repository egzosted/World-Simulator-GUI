from abc import ABC, abstractmethod
from Organisms.Organism import Organism
import random


class Plant(Organism, ABC):
    def __init__(self):
        super(Plant, self).__init__(self)
        self._nextX = None
        self._nextY = None

    def action(self, world):
        reproduction = random.randint(1, 100)
        if reproduction <= 5:  # plants have 5% chance to reproduce
            self.try_reproduce(world)

    def try_reproduce(self, world):
        if self.is_empty(self.get_x(), self.get_y(), world):
            world.report += self.get_name()
            world.report += " has been sown\n"
            o = self.create_clone()
            o.set_adulthood(False)
            o.set_x(world.get_first_coordinate())
            o.set_y(world.get_second_coordinate())
            world.isOccupied[o.get_x()][o.get_y()] = 1
            world.add_organism(o)

    def collision(self, world, offender):
        world.report += self.get_name()
        world.report += " ate by "
        world.report += offender.get_name()
        world.report += "\n"
        world.isOccupied[offender.get_x()][offender.get_y()] = 0
        self.deleteMe = 1
        offender.set_x(self.get_x())
        offender.set_y(self.get_y())

    def poisoning_collision(self, world, offender):
        world.report += self.get_name()
        world.report += " ate by "
        world.report += offender.get_name()
        world.report += "\n"
        world.report += offender.get_name()
        world.report += " poisoned by "
        world.report += self.get_name()
        world.report += "\n"
        world.isOccupied[offender.get_x()][offender.get_y()] = 0
        world.isOccupied[self.get_x()][self.get_y()] = 0
        if offender.get_name() == "Human":
            world.mark_end()
        offender.deleteMe = 1
        self.deleteMe = 1

    @abstractmethod
    def create_clone(self):
        pass
