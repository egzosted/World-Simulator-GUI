from Organisms.Animal import Animal
import copy
import random


class Turtle(Animal):
    def __init__(self, x, y, world):
        super(Animal, self).__init__()
        self._name = "Turtle"
        self._symbol = "T"
        self._power = 2
        self._courage = 1
        self._positionX = x
        self._positionY = y
        self._backgroundColor = "blue"  # wolf has white symbol on gray background
        self._foregroundColor = "white"
        world.isOccupied[self._positionX][self._positionY] = 1

    def action(self, world):
        movement = random.randint(1, 100)
        if movement > 75:  # turtle has 75% probability to move from his field
            super(Turtle, self).action(world)

    def collision(self, world, offender):
        is_dead = self.did_die(offender)
        if is_dead == 1:
            self.offender_won(world, offender)
        elif self._name == offender.get_name():
            self.reproduce(world)
        else:
            world.report += "Turtle has been unsuccessfully attacked by "
            world.report += offender.get_name()
            world.report += "\n"

    def did_die(self, offender):
        if offender.get_power() < 5:  # turtle defends from weak opponents that have less than 5 power
            return 0
        return 1

    def create_clone(self):
        return copy.deepcopy(self)