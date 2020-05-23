from Organisms.Animal import Animal
import copy
import random


class Antelope(Animal):
    def __init__(self, x, y, world):
        super(Animal, self).__init__()
        self._name = "Antelope"
        self._symbol = "A"
        self._power = 4
        self._courage = 4
        self._positionX = x
        self._positionY = y
        self._backgroundColor = "cyan"  # antelope has white symbol on cyan background
        self._foregroundColor = "white"
        self.__WALK = 0
        self.__JUMP = 1
        world.isOccupied[self._positionX][self._positionY] = 1

    def action(self, world):
        jump = 0
        found = 0
        direction = 0
        while found == 0:
            direction = random.randint(0,3)
            jump = random.randint(0,1)
            found = self.is_movement_inside_ant(world, direction, jump)
        if jump == self.__WALK:
            self.set_next_xy(direction)
        else:
            self.set_jump_xy(direction)
        self.move(world)

    def is_movement_inside_ant(self, world, direction, jump):
        found = 0
        if direction == self._LEFT and jump == self.__JUMP:
            found = self.is_inside(self._positionX, self._positionY - 2, world.get_height(), world.get_width())
        elif direction == self._LEFT and jump == self.__WALK:
            found = self.is_inside(self._positionX, self._positionY - 1, world.get_height(), world.get_width())
        elif direction == self._RIGHT and jump == self.__JUMP:
            found = self.is_inside(self._positionX, self._positionY + 2, world.get_height(), world.get_width())
        elif direction == self._RIGHT and jump == self.__WALK:
            found = self.is_inside(self._positionX, self._positionY + 1, world.get_height(), world.get_width())
        elif direction == self._UP and jump == self.__JUMP:
            found = self.is_inside(self._positionX - 2, self._positionY, world.get_height(), world.get_width())
        elif direction == self._UP and jump == self.__WALK:
            found = self.is_inside(self._positionX - 1, self._positionY, world.get_height(), world.get_width())
        elif direction == self._DOWN and jump == self.__JUMP:
            found = self.is_inside(self._positionX + 2, self._positionY, world.get_height(), world.get_width())
        elif direction == self._DOWN and jump == self.__WALK:
            found = self.is_inside(self._positionX + 1, self._positionY, world.get_height(), world.get_width())
        return found

    def set_jump_xy(self, direction):
        if direction == self._LEFT:
            self._nextX = self._positionX
            self._nextY = self._positionY - 2
        elif direction == self._RIGHT:
            self._nextX = self._positionX
            self._nextY = self._positionY + 2
        elif direction == self._UP:
            self._nextX = self._positionX - 2
            self._nextY = self._positionY
        else:
            self._nextX = self._positionX + 2
            self._nextY = self._positionY

    def escape(self, world):
        found_place = self.is_empty(self.get_x(), self.get_y(), world)
        if found_place == False:
            return 0
        return 1

    def collision(self, world, offender):
        escape = random.randint(1, 100)
        successfulEscape = 0
        if escape > 50:  # if antelope is defender it has 50% chance to avoid fight
            successfulEscape = self.escape(world)
        if self.get_name() == offender.get_name():
            self.reproduce(world)
        elif escape <= 50 or (escape > 50 and successfulEscape == 0):
            is_dead = self.did_die(offender)
            if is_dead == 0:
                self.defender_won(world, offender)
            else:
                self.offender_won(world, offender)
        else:
            world.isOccupied[world.get_first_coordinate()][world.get_second_coordinate()] = 1
            world.isOccupied[offender.get_x()][offender.get_y()] = 0
            offender.set_x(self.get_x())
            offender.set_y(self.get_y())
            self.set_x(world.get_first_coordinate())
            self.set_y(world.get_second_coordinate())

    def create_clone(self):
        return copy.deepcopy(self)