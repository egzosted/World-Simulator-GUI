import random
import pickle
from Organisms import Wolf
from Organisms import Sheep
from Organisms import Human
from Organisms import Turtle
from Organisms import Fox
from Organisms import Antelope
from Organisms import Grasp
from Organisms import Yellow
from Organisms import Guarana
from Organisms import WolfBerries
from Organisms import KillerSosnowskyi
from Organisms import CyberSheep


class World:

    def __init__(self):
        self.coordinates = [0] * 2  # 2 element list to rand coordinates of organism
        self.__end = False
        self.report = ""  # in every round we note most important events
        self.__round = 1
        self.__width = None
        self.__height = None
        self.__initialPopulation = None
        self.__direction = None
        self.__human = None  # we need reference for human to turn on ultimate at the beginning of round
        self.LEFT = 0  # variables defining direction
        self.RIGHT = 1
        self.UP = 2
        self.DOWN = 3
        self.isOccupied = None  # 2d list that tells if field is occupied by organism
        self.organisms = []   # list of objects type organism

    def rand_coordinates(self):  # creates random coordinates for organism
        self.coordinates[0] = random.randint(0, self.__height - 1)
        self.coordinates[1] = random.randint(0, self.__width - 1)
        if self.isOccupied[self.coordinates[0]][self.coordinates[1]] == 1:
            self.rand_coordinates()

    def add_organism(self, o):
        length = len(self.organisms)
        for i in range(length):
            if self.organisms[i].get_courage() < o.get_courage():
                self.organisms.insert(i, o)
                return
        self.organisms.append(o)

    # def delete_organism(self, x, y):
    #     length = len(self.organisms)
    #     for i in range(length):
    #         if self.organisms[i].get_x() == x and self.organisms[i].get_y() == y:
    #             del self.organisms[i]
    #             return

    def find_human(self):
        length = len(self.organisms)
        for i in range(length):
            if self.organisms[i].get_name() == "Human":
                return self.organisms[i]

    def delete_organisms(self):
        iterator = 0
        length = len(self.organisms)
        for i in range(length):
            if self.organisms[iterator].deleteMe == 1:
                self.organisms.pop(iterator)
                iterator -= 1
            iterator += 1

    def perform_board(self, direction, ultimate):
        self.increment_round()
        self.report = ""
        if ultimate == 1:
            self.__human.turn_on_ultimate()
        self.__direction = direction
        if self.check_direction() == 0:
            return 0

        for i in self.organisms:
            if i.get_adulthood() and i.deleteMe == 0:
                i.action(self)

        self.delete_organisms()

        for i in self.organisms:
            i.set_adulthood(True)

    def add_start_animals(self):
        for i in range(self.__initialPopulation):
            self.rand_coordinates()
            h = Fox.Fox(self.get_first_coordinate(), self.get_second_coordinate(), self)
            self.organisms.append(h)
            self.isOccupied[self.get_first_coordinate()][self.get_second_coordinate()] = 1

        for i in range(self.__initialPopulation):
            self.rand_coordinates()
            h = Wolf.Wolf(self.get_first_coordinate(), self.get_second_coordinate(), self)
            self.organisms.append(h)
            self.isOccupied[self.get_first_coordinate()][self.get_second_coordinate()] = 1

        for i in range(self.__initialPopulation):
            self.rand_coordinates()
            h = Sheep.Sheep(self.get_first_coordinate(), self.get_second_coordinate(), self)
            self.organisms.append(h)
            self.isOccupied[self.get_first_coordinate()][self.get_second_coordinate()] = 1

        self.rand_coordinates()
        h = Human.Human(self.get_first_coordinate(), self.get_second_coordinate(), self)
        self.organisms.append(h)
        self.isOccupied[self.get_first_coordinate()][self.get_second_coordinate()] = 1
        self.__human = h

        for i in range(self.__initialPopulation):
            self.rand_coordinates()
            h = CyberSheep.CyberSheep(self.get_first_coordinate(), self.get_second_coordinate(), self)
            self.organisms.append(h)
            self.isOccupied[self.get_first_coordinate()][self.get_second_coordinate()] = 1

        for i in range(self.__initialPopulation):
            self.rand_coordinates()
            h = Antelope.Antelope(self.get_first_coordinate(), self.get_second_coordinate(), self)
            self.organisms.append(h)
            self.isOccupied[self.get_first_coordinate()][self.get_second_coordinate()] = 1

        for i in range(self.__initialPopulation):
            self.rand_coordinates()
            h = Turtle.Turtle(self.get_first_coordinate(), self.get_second_coordinate(), self)
            self.organisms.append(h)
            self.isOccupied[self.get_first_coordinate()][self.get_second_coordinate()] = 1

        for i in range(self.__initialPopulation):
            self.rand_coordinates()
            h = Guarana.Guarana(self.get_first_coordinate(), self.get_second_coordinate(), self)
            self.organisms.append(h)
            self.isOccupied[self.get_first_coordinate()][self.get_second_coordinate()] = 1

        for i in range(self.__initialPopulation):
            self.rand_coordinates()
            h = Yellow.Yellow(self.get_first_coordinate(), self.get_second_coordinate(), self)
            self.organisms.append(h)
            self.isOccupied[self.get_first_coordinate()][self.get_second_coordinate()] = 1

        for i in range(self.__initialPopulation):
            self.rand_coordinates()
            h = Grasp.Grasp(self.get_first_coordinate(), self.get_second_coordinate(), self)
            self.organisms.append(h)
            self.isOccupied[self.get_first_coordinate()][self.get_second_coordinate()] = 1

        for i in range(self.__initialPopulation):
            self.rand_coordinates()
            h = WolfBerries.WolfBerries(self.get_first_coordinate(), self.get_second_coordinate(), self)
            self.organisms.append(h)
            self.isOccupied[self.get_first_coordinate()][self.get_second_coordinate()] = 1

        for i in range(self.__initialPopulation):
            self.rand_coordinates()
            h = KillerSosnowskyi.KillerSosnowskyi(self.get_first_coordinate(), self.get_second_coordinate(), self)
            self.organisms.append(h)
            self.isOccupied[self.get_first_coordinate()][self.get_second_coordinate()] = 1

    def save(self, filename):
        dat_name = filename + ".dat"
        txt_name = filename + ".txt"
        txt_outfile = open(txt_name, 'w')
        txt_outfile.write(str(self.get_height()) + '\n')
        txt_outfile.write(str(self.get_width())+ '\n')
        txt_outfile.write(str(self.get_round()) + '\n')
        for i in range(self.get_height()):
            for j in range(self.get_width()):
                txt_outfile.write(str(self.isOccupied[i][j]) + '\n')
        txt_outfile.close()

        dat_outfile = open(dat_name, 'wb')
        for i in self.organisms:
            pickle.dump(i, dat_outfile)
        dat_outfile.close()

    def load(self, filename):
        dat_name = filename + ".dat"
        txt_name = filename + ".txt"
        txt_infile = open(txt_name, 'r')
        self.__height = int(txt_infile.readline())
        self.__width = int(txt_infile.readline())
        self.__round = int(txt_infile.readline())
        self.set_flags()
        for i in range(self.get_height()):
            for j in range(self.get_width()):
                self.isOccupied[i][j] = int(txt_infile.readline())
        txt_infile.close()

        end_of_file = False
        self.organisms = []
        dat_infile = open(dat_name, 'rb')
        while not end_of_file:
            try:
                o = pickle.load(dat_infile)
                self.organisms.append(o)
            except EOFError:
                end_of_file = True
        dat_infile.close()

    def set_flags(self):    # this method is used to set default value of occupation on every field
        self.isOccupied = [[0] * self.__width for i in range(self.__height)]

    def set_width(self, w):
        self.__width = w

    def set_height(self, h):
        self.__height = h

    def set_initial_population(self, i):
        self.__initialPopulation = i

    def increment_round(self):
        self.__round += 1

    def mark_end(self):
        self.__end = True

    def set_round(self, r):
        self.__round = r

    def set_direction(self, s):
        self.__direction = s

    def set_coordinates(self, x, y):
        self.coordinates[0] = x
        self.coordinates[1] = y

    def get_size_organisms(self):
        return len(self.organisms)

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_direction(self):
        return self.__direction

    def get_round(self):
        return self.__round

    def is_end(self):
        return self.__end

    def get_first_coordinate(self):
        return self.coordinates[0]

    def get_second_coordinate(self):
        return self.coordinates[1]

    def get_human(self):
        return self.__human

    def set_human(self, o):
        self.__human = o

    def check_direction(self):
        if self.__direction < self.LEFT or self.__direction > self.DOWN:
            return 0
        return 1
