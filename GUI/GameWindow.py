from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import World.World as World


NUMBER_OF_SPECIES = 11


class GameWindow:
    def __init__(self):
        self.__root = Tk()  # main window of game
        self.__World = World.World()  # creates new world
        self.__ultimate = 0  # waiting for user to press R
        self.__SAVE = 0
        self.__LOAD = 1
        self.__e_filename = None
        self.__operation = None
        self.__b_submit_filename = None
        # before start of game user has to enter size of board and initial population of species
        self.__lHeight = Label(self.__root, text="Enter height of board ", bg="black", fg="white")
        self.__lWidth = Label(self.__root, text="Enter width of board ", bg="black", fg="white")
        self.__lInitialPopulation = Label(
            self.__root, text="Enter initial population of species ", bg="black", fg="white")
        self.__eHeight = Entry(self.__root)
        self.__eWidth = Entry(self.__root)
        self.__eInitialPopulation = Entry(self.__root)
        self.__bStart = Button(self.__root, text="Start", bg="yellow",
                               fg="blue", command=self.__start_game)

        # placing components using grid layout
        self.__lHeight.grid(row=0, column=0)
        self.__lWidth.grid(row=1, column=0)
        self.__lInitialPopulation.grid(row=2, column=0)
        self.__eHeight.grid(row=0, column=1)
        self.__eWidth.grid(row=1, column=1)
        self.__eInitialPopulation.grid(row=2, column=1)
        self.__bStart.grid(row=3, columnspan=2)
        self.__root.mainloop()

        # array of buttons
        self.__icons = None

        # later used buttons
        self.__bSave = None
        self.__bLoad = None
        self.__bReport = None

    def __start_game(self):
        # first we assign size of board entered by user
        height = int(self.__eHeight.get())
        width = int(self.__eWidth.get())
        initial_population = int(self.__eInitialPopulation.get())
        self.__World.set_height(height)
        self.__World.set_width(width)
        self.__World.set_initial_population(initial_population)
        self.__World.set_flags()

        if height * width < initial_population * NUMBER_OF_SPECIES + 1:
            self.__lTooSmall = Label(self.__root, text="Our organisms need more space")
            self.__lTooSmall.grid(row=4, columnspan=2)
            return

        self.__World.add_start_animals()

        # then we delete unnecessary widgets
        start_widgets = self.__root.grid_slaves()
        for l in start_widgets:
            l.destroy()

        # new view of buttons
        self.__create_organism_buttons(height, width)
        self.__color_buttons(height, width)

        # functional buttons
        self.__bLoad = Button(self.__root, text="Load game", bg="gray30", command=self.load)
        self.__bSave = Button(self.__root, text="Save game", bg="gray30", command=self.save)
        self.__bReport = Button(self.__root, text="Report game",
                                bg="gray30", command=self.show_report)
        self.__bLoad.grid(row=height, column=0, columnspan=width // 3, sticky=N + S + E + W)
        self.__bSave.grid(row=height, column=width // 3,
                          columnspan=width // 3, sticky=N + S + E + W)
        if width % 3 == 0:
            self.__bReport.grid(row=height, column=2*(width//3),
                                columnspan=width//3, sticky=N+S+E+W)
        else:
            self.__bReport.grid(row=height, column=2*(width//3),
                                columnspan=width//3+width % 3, sticky=N+S+E+W)

        # binding functional keys
        self.__root.bind('<Up>', lambda event: self.move_up())
        self.__root.bind('<Down>', lambda event: self.move_down())
        self.__root.bind('<Left>', lambda event: self.move_left())
        self.__root.bind('<Right>', lambda event: self.move_right())
        self.__root.bind('g', lambda event: self.show_report())
        self.__root.bind('r', lambda event: self.ulti())
        self.__root.bind('s', lambda event: self.stats())

    def __create_organism_buttons(self, height, width):
        self.icons = [[Button()] * width for i in range(height)]
        for i in range(height):
            for j in range(width):
                self.icons[i][j] = Button(self.__root, text="",
                                          command=lambda x=i, y=j: self.add_existing_organism(x, y))
                self.icons[i][j].grid(row=i, column=j, sticky=N+S+E+W)

        for x in range(width):
            Grid.columnconfigure(self.__root, x, weight=1)

        for y in range(height):
            Grid.rowconfigure(self.__root, y, weight=1)

    def __color_buttons(self, height, width):
        if len(self.__World.organisms) > 0:
            for i in range(len(self.__World.organisms)):
                if self.__World.organisms[i] == 1:
                    continue
                x = self.__World.organisms[i].get_x()
                y = self.__World.organisms[i].get_y()
                self.icons[x][y].config(bg=self.__World.organisms[i].get_background_color())
                self.icons[x][y].config(fg=self.__World.organisms[i].get_foreground_color())
                self.icons[x][y].config(text=self.__World.organisms[i].get_symbol())

        for i in range(height):
            for j in range(width):
                if self.__World.isOccupied[i][j] == 0:
                    self.icons[i][j].config(bg="gray90", text="")

        if self.__World.is_end():
            messagebox.showinfo("End of game", "You died!")
            self.__root.unbind('s')
            self.__root.unbind('r')

    def move_up(self):
        if self.__World.is_end() == False:
            self.__World.perform_board(self.__World.UP, self.__ultimate)
            self.__ultimate = 0
            self.__color_buttons(self.__World.get_height(), self.__World.get_width())

    def move_down(self):
        if self.__World.is_end() == False:
            self.__World.perform_board(self.__World.DOWN, self.__ultimate)
            self.__ultimate = 0
            self.__color_buttons(self.__World.get_height(), self.__World.get_width())

    def move_left(self):
        if self.__World.is_end() == False:
            self.__World.perform_board(self.__World.LEFT, self.__ultimate)
            self.__ultimate = 0
            self.__color_buttons(self.__World.get_height(), self.__World.get_width())

    def move_right(self):
        if self.__World.is_end() == False:
            self.__World.perform_board(self.__World.RIGHT, self.__ultimate)
            self.__ultimate = 0
            self.__color_buttons(self.__World.get_height(), self.__World.get_width())

    def load(self):
        if self.__World.is_end() == False:
            self.__operation = self.__LOAD
            self.enter_filename(self.__LOAD)

    def save(self):
        if self.__World.is_end() == False:
            self.__operation = self.__SAVE
            self.enter_filename(self.__SAVE)

    def show_report(self):
        w_report = Tk()
        t_report = Text(w_report)
        t_report.config(font=("Courier", 25))
        t_report.insert(END, self.__World.report)
        t_report.pack(side=LEFT)
        w_report.mainloop()

    def stats(self):  # user can look at round and his power, also there is option see when ultimate will be available
        w_stats = Tk()
        message = "Round: "
        message += str(self.__World.get_round())
        message += "\nPower: "
        human = self.__World.get_human()
        message += str(human.get_power())
        message += "\n"
        if human.get_end_ultimate() > human.ULTIMATE_DURATION:
            message += "Ultimate turned on: "
            message += str(human.NEXT_ULTIMATE - human.get_end_ultimate())
            message += " round(s)!\n"

        if human.get_end_ultimate() <= human.ULTIMATE_DURATION:
            message += "Ultimate available in: "
            message += str(human.get_end_ultimate())
            message += " round(s)!\n"
        t_message = Text(w_stats)
        t_message.config(font=("Courier", 25))
        t_message.insert(END, message)
        t_message.pack(side=LEFT)
        w_stats.mainloop()

    def ulti(self):
        self.__ultimate = 1

    def add_existing_organism(self, x, y):
        if self.__World.isOccupied[x][y] == 1:
            return
        for i in range(self.__World.get_height()):
            for j in range(self.__World.get_width()):
                self.icons[i][j].grid_remove()
        self.__bLoad.grid_remove()
        self.__bSave.grid_remove()
        self.__bReport.grid_remove()

        strings = []
        for i in self.__World.organisms:
            if i.get_name() == "Human" or i.deleteMe == 1:
                continue
            name = i.get_name()
            found = 0
            for j in range(len(strings)):
                if strings[j] == name:
                    found = 1
                    break
            if found == 0:
                strings.append(name)

        combo = ttk.Combobox(self.__root, values=strings)
        combo.current(0)
        combo.bind("<<ComboboxSelected>>", lambda event: self.combo_callback(combo, x, y))
        combo.grid()

    def combo_callback(self, combo, x, y):
        for i in range(self.__World.get_height()):
            for j in range(self.__World.get_width()):
                self.icons[i][j].grid()
        self.__bLoad.grid()
        self.__bSave.grid()
        self.__bReport.grid()
        o = None
        for i in self.__World.organisms:
            if combo.get() == i.get_name() and i.deleteMe == 0:
                o = i.create_clone()
                break
        o.set_x(x)
        o.set_y(y)
        self.__World.isOccupied[x][y] = 1
        self.__World.add_organism(o)
        self.__color_buttons(self.__World.get_height(), self.__World.get_width())
        combo.destroy()

    def enter_filename(self, operation):
        self.__root.unbind('s')
        self.__root.unbind('r')
        self.__root.unbind('g')
        for i in range(self.__World.get_height()):
            for j in range(self.__World.get_width()):
                self.icons[i][j].grid_remove()
        self.__bLoad.grid_remove()
        self.__bSave.grid_remove()
        self.__bReport.grid_remove()
        self.__e_filename = Entry(self.__root)
        self.__b_submit_filename = Button(
            self.__root, text="Submit", command=self.perform_file_operation)
        self.__e_filename.grid()
        self.__b_submit_filename.grid()

    def perform_file_operation(self):
        if self.__operation == self.__SAVE:
            self.__World.save(self.__e_filename.get())
            self.__e_filename.grid_remove()
            self.__b_submit_filename.grid_remove()
            for i in range(self.__World.get_height()):
                for j in range(self.__World.get_width()):
                    self.icons[i][j].grid()
            self.__bLoad.grid()
            self.__bSave.grid()
            self.__bReport.grid()

        if self.__operation == self.__LOAD:
            self.__World.load(self.__e_filename.get())
            self.__e_filename.grid_remove()
            self.__b_submit_filename.grid_remove()
            self.icons = None
            self.icons = [[Button()] * self.__World.get_width()
                          for i in range(self.__World.get_height())]
            for i in range(self.__World.get_height()):
                for j in range(self.__World.get_width()):
                    self.icons[i][j] = Button(self.__root, text="",
                                              command=lambda x=i, y=j: self.add_existing_organism(x, y))
                    self.icons[i][j].grid(row=i, column=j, sticky=N + S + E + W)
            for x in range(self.__World.get_width()):
                Grid.columnconfigure(self.__root, x, weight=1)

            for y in range(self.__World.get_height()):
                Grid.rowconfigure(self.__root, y, weight=1)

            self.__bLoad.grid(row=self.__World.get_height(), column=0,
                              columnspan=self.__World.get_width() // 3, sticky=N + S + E + W)
            self.__bSave.grid(row=self.__World.get_height(), column=self.__World.get_width(
            ) // 3, columnspan=self.__World.get_width() // 3, sticky=N + S + E + W)
            if self.__World.get_width() % 3 == 0:
                self.__bReport.grid(row=self.__World.get_height(
                ), column=2 * (self.__World.get_width() // 3), columnspan=self.__World.get_width() // 3, sticky=N + S + E + W)
            else:
                self.__bReport.grid(row=self.__World.get_height(), column=2 * (self.__World.get_width() // 3),
                                    columnspan=self.__World.get_width() // 3 + self.__World.get_width() % 3,  sticky=N + S + E + W)
        self.__root.bind('g', lambda event: self.show_report())
        self.__root.bind('r', lambda event: self.ulti())
        self.__root.bind('s', lambda event: self.stats())
        self.__color_buttons(self.__World.get_height(), self.__World.get_width())
        self.__World.set_human(self.__World.find_human())
