from person import Person


class Bomberman(Person):

    def __init__(self, structure):
        self.x = 2
        self.y = 4
        self.structure = structure

        self.shape = [[0 for x in range(4)] for y in range(2)]

        self.shape = [['B', 'B', 'B', 'B'], ['B', 'B', 'B', 'B']]

        for i in range(2):
            for j in range(4):
                self.structure[i + 2][j + 4] = self.shape[i][j]

        self.lives = 3

    def display_with_bomberman(self):
        for i in range(0, 42):
            for j in range(0, 84):
                print(self.structure[i][j], end="")
            print()

    def die_respawn(self):

        if self.structure[self.x][self.y] == '^' or self.structure[self.x][self.y] == 'E':
            self.x = 2
            self.y = 4
            self.lives = self.lives - 1

            for j in range(0, 2):
                for i in range(0, 4):
                    self.structure[self.x + j][self.y + i] = self.shape[j][i]

    def up_respawn(self):

        if self.structure[self.x -
                          2][self.y] == '^' or self.structure[self.x - 2][self.y] == 'E':

            for j in range(0, 2):
                for i in range(0, 4):
                    self.structure[self.x + j][self.y + i] = " "

            self.x = 2
            self.y = 4
            self.lives = self.lives - 1

            for j in range(0, 2):
                for i in range(0, 4):
                    self.structure[self.x + j][self.y + i] = self.shape[j][i]
            return 1

        else:
            return 0

    def down_respawn(self):

        if self.structure[self.x +
                          2][self.y] == '^' or self.structure[self.x + 2][self.y] == 'E':

            for j in range(0, 2):
                for i in range(0, 4):
                    self.structure[self.x + j][self.y + i] = " "

            self.x = 2
            self.y = 4
            self.lives = self.lives - 1

            for j in range(0, 2):
                for i in range(0, 4):
                    self.structure[self.x + j][self.y + i] = self.shape[j][i]
            return 1

        else:
            return 0

    def right_respawn(self):

        if self.structure[self.x][self.y +
                                  4] == '^' or self.structure[self.x][self.y + 4] == 'E':

            for j in range(0, 2):
                for i in range(0, 4):
                    self.structure[self.x + j][self.y + i] = " "

            self.x = 2
            self.y = 4
            self.lives = self.lives - 1

            for j in range(0, 2):
                for i in range(0, 4):
                    self.structure[self.x + j][self.y + i] = self.shape[j][i]
            return 1

        else:
            return 0

    def left_respawn(self):

        if self.structure[self.x][self.y -
                                  4] == '^' or self.structure[self.x][self.y - 4] == 'E':

            for j in range(0, 2):
                for i in range(0, 4):
                    self.structure[self.x + j][self.y + i] = " "

            self.x = 2
            self.y = 4
            self.lives = self.lives - 1

            for j in range(0, 2):
                for i in range(0, 4):
                    self.structure[self.x + j][self.y + i] = self.shape[j][i]
            return 1

        else:
            return 0
