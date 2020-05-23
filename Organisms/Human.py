from Organisms.Animal import Animal
import copy


class Human(Animal):
    def __init__(self, x, y, world):
        super(Animal, self).__init__()
        self._name = "Human"
        self._symbol = "H"
        self._power = 5
        self._courage = 4
        self._positionX = x
        self._positionY = y
        self.__startUltimate = 0    # idea of ultimate algorithm: we have 2 variables, that "measure" difference between and start, if we turn on ultimate, we set end on 10
        self.__endUltimate = 0   # and then we decrement this value in every round 5 rounds of ultimate time duration and 5 rounds waiting for next ultimate
        self.__POWER_BONUS = 5
        self.NEXT_ULTIMATE = 10
        self.ULTIMATE_DURATION = 5
        self.__ENABLED = 0
        self._backgroundColor = "black"  # human has white symbol on black background
        self._foregroundColor = "white"
        world.isOccupied[self._positionX][self._positionY] = 1

    def turn_on_ultimate(self):
        if self.__startUltimate == self.__endUltimate:
            self._power += self.__POWER_BONUS
            self.__endUltimate = 10

    def handle_ultimate(self):
        if self.__endUltimate > self.ULTIMATE_DURATION and self.__endUltimate <= self.NEXT_ULTIMATE:
            self._power -= 1

        if self.__endUltimate > self.__ENABLED:
            self.__endUltimate -= 1

    def action(self, world):
        direction = world.get_direction()
        if self.is_movement_inside(world, direction) == 0:
            return
        self.set_next_xy(direction)
        self.move(world)
        self.handle_ultimate()

    def get_end_ultimate(self):
        return self.__endUltimate

    def create_clone(self):
        return copy.deepcopy(self)
