from Organisms.Animal import Animal
import copy
import random


class Fox(Animal):
    def __init__(self, x, y, world):
        super(Animal, self).__init__()
        self._name = "Fox"
        self._symbol = "F"
        self._power = 3
        self._courage = 7
        self._positionX = x
        self._positionY = y
        self._backgroundColor = "orange"  # fox has white symbol on orange background
        self._foregroundColor = "white"
        world.isOccupied[self._positionX][self._positionY] = 1

    def action(self, world):
        found = 0
        iteration = 0
        while found == 0 and iteration < 1000:  # generally fox can't move on field where is stronger opponent, so
            direction = random.randint(0, 3)  # I assume that if we can't find him opponent in 1000
            if direction == self._LEFT:  # rounds then fox has to stay on his position
                found = self.is_movement_inside(world, direction)
                if found == 1:
                    self._nextX = self._positionX
                    self._nextY = self._positionY - 1
                    found = self.find_safe_place(world, self._nextX, self._nextY)

            if direction == self._RIGHT:
                found = self.is_movement_inside(world, direction)
                if found == 1:
                    self._nextX = self._positionX
                    self._nextY = self._positionY + 1
                    found = self.find_safe_place(world, self._nextX, self._nextY)

            if direction == self._UP:
                found = self.is_movement_inside(world, direction)
                if found == 1:
                    self._nextX = self._positionX - 1
                    self._nextY = self._positionY
                    found = self.find_safe_place(world, self._nextX, self._nextY)

            if direction == self._DOWN:
                found = self.is_movement_inside(world, direction)
                if found == 1:
                    self._nextX = self._positionX + 1
                    self._nextY = self._positionY
                    found = self.find_safe_place(world, self._nextX, self._nextY)

            if found == 1:
                self.set_next_xy(direction)
                self.move(world)
            iteration += 1

    def find_safe_place(self, world, next_x, next_y):
        o = None
        for i in world.organisms:
            if i.get_x() == next_x and i.get_y() == next_y and i.deleteMe == 0:
                o = i
                break
        if o is not None and self._power < o.get_power():
            return 0
        return 1

    def create_clone(self):
        return copy.deepcopy(self)