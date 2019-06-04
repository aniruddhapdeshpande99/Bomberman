class Person():

    def __init__(self, x, y, structure):
        self.x = x
        self.y = y
        self.structure = structure
        self.shape = [[0 for x in range(4)] for y in range(2)]

    def move_right(self):

        x = self.x
        y = self.y

        if self.structure[self.x][self.y + 4] == " " or self.structure[self.x][self.y +
                                                                               5] == "^" or self.structure[self.x][self.y + 4] == "^" or self.structure[self.x][self.y + 4] == "{":

            for j in range(0, 2):
                for i in range(0, 4):
                    self.structure[self.x + j][self.y + i] = " "

            self.y = self.y + 4

            for j in range(0, 2):
                for i in range(0, 4):
                    self.structure[self.x + j][self.y + i] = self.shape[j][i]

    def move_left(self):

        x = self.x
        y = self.y

        if self.structure[self.x][self.y - 4] == " " or self.structure[self.x][self.y -
                                                                               3] == "^" or self.structure[self.x][self.y - 4] == "^" or self.structure[self.x][self.y - 4] == "{":

            for j in range(0, 2):
                for i in range(0, 4):
                    self.structure[self.x + j][self.y + i] = " "

            self.y = self.y - 4

            for j in range(0, 2):
                for i in range(0, 4):
                    self.structure[self.x + j][self.y + i] = self.shape[j][i]

    def move_down(self):

        x = self.x
        y = self.y

        if self.structure[self.x + 2][self.y] == " " or self.structure[self.x + 2][self.y +
                                                                                   1] == "^" or self.structure[self.x + 2][self.y] == "^" or self.structure[self.x + 2][self.y] == "{":

            for j in range(0, 2):
                for i in range(0, 4):
                    self.structure[self.x + j][self.y + i] = " "

            self.x = self.x + 2

            for j in range(0, 2):
                for i in range(0, 4):
                    self.structure[self.x + j][self.y + i] = self.shape[j][i]

    def move_up(self):

        x = self.x
        y = self.y

        if self.structure[self.x - 2][self.y] == " " or self.structure[self.x - 2][self.y +
                                                                                   1] == "^" or self.structure[self.x - 2][self.y] == "^" or self.structure[self.x - 2][self.y] == "{":

            for j in range(0, 2):
                for i in range(0, 4):
                    self.structure[self.x + j][self.y + i] = " "

            self.x = self.x - 2

            for j in range(0, 2):
                for i in range(0, 4):
                    self.structure[self.x + j][self.y + i] = self.shape[j][i]
