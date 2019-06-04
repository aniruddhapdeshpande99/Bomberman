import time
import os


class Bomb():

    def __init__(self, structure, x, y):
        self.structure = structure
        self.x = x
        self.y = y
        self.shape = [['[', ' ', ' ', ']'], ['[', ' ', ' ', ']']]
        self.time = time.time()
        self.flag = 0

    def create_bomb(self, structure):

        for j in range(0, 2):
            for i in range(0, 4):
                self.structure[self.x + j][self.y + i] = self.shape[j][i]

    def tick(self, structure, num):

        self.shape[0][1] = 3 - num
        self.shape[0][2] = 3 - num
        self.shape[1][1] = 3 - num
        self.shape[1][2] = 3 - num

        for j in range(0, 2):
            for i in range(0, 4):
                self.structure[self.x + j][self.y + i] = self.shape[j][i]

    def explode(self, structure):

        score = 0

        for j in range(0, 2):
            for i in range(0, 4):
                self.shape[j][i] = '^'
                self.structure[self.x + j][self.y + i] = self.shape[j][i]

        if structure[self.x - 2][self.y] != '#':
            if structure[self.x - 2][self.y] == '/':
                score = score + 20

            for j in range(0, 2):
                for i in range(0, 4):
                    self.shape[j][i] = '^'
                    self.structure[self.x - 2 + j][self.y + i] = '^'

        if structure[self.x + 2][self.y] != '#':

            if structure[self.x + 2][self.y] == '/':
                score = score + 20

            for j in range(0, 2):
                for i in range(0, 4):
                    self.shape[j][i] = '^'
                    self.structure[self.x + 2 + j][self.y + i] = '^'

        if structure[self.x][self.y + 4] != '#':

            if structure[self.x][self.y + 4] == '/':
                score = score + 20

            for j in range(0, 2):
                for i in range(0, 4):
                    self.shape[j][i] = '^'
                    self.structure[self.x + j][self.y + 4 + i] = '^'

        if structure[self.x][self.y - 4] != '#':

            if structure[self.x][self.y - 4] == '/':
                score = score + 20

            for j in range(0, 2):
                for i in range(0, 4):
                    self.shape[j][i] = '^'
                    self.structure[self.x + j][self.y - 4 + i] = '^'

        self.flag = 1
        return score

    def vanish(self, structure):

        for j in range(0, 2):
            for i in range(0, 4):
                self.shape[j][i] = ' '
                self.structure[self.x + j][self.y + i] = ' '

        if structure[self.x - 2][self.y] != '#':
            for j in range(0, 2):
                for i in range(0, 4):
                    self.shape[j][i] = ' '
                    self.structure[self.x - 2 + j][self.y + i] = ' '

        if structure[self.x + 2][self.y] != '#':
            for j in range(0, 2):
                for i in range(0, 4):
                    self.shape[j][i] = ' '
                    self.structure[self.x + 2 + j][self.y + i] = ' '

        if structure[self.x][self.y + 4] != '#':
            for j in range(0, 2):
                for i in range(0, 4):
                    self.shape[j][i] = ' '
                    self.structure[self.x + j][self.y + 4 + i] = ' '

        if structure[self.x][self.y - 4] != '#':
            for j in range(0, 2):
                for i in range(0, 4):
                    self.shape[j][i] = ' '
                    self.structure[self.x + j][self.y - 4 + i] = ' '
