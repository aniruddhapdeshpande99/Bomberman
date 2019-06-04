from person import Person
import random


class Enemy(Person):

    def __init__(self, structure):
        self.structure = structure
        self.x = 0
        self.y = 0
        self.shape = [['E', 'E', 'E', 'E'], ['E', 'E', 'E', 'E']]
        self.flag = 1

    def create_enemy(self, enemy_x, enemy_y, structure):

        self.x = enemy_x
        self.y = enemy_y

        for j in range(0, 2):
            for i in range(0, 4):
                self.structure[enemy_x + j][enemy_y + i] = self.shape[j][i]

    def place_enemy(self, structure):
        enemy_count = 0
        while True:
            y = random.randint(4, 76)
            x = random.randint(2, 38)
            flag = 1

            if x % 4 == 2 and (y % 8 == 0 or y %
                               8 == 4) and structure[x][y] == ' ':
                flag = 1
            elif x % 4 == 0 and y % 8 == 4 and structure[x][y] == ' ':
                flag = 1
            else:
                flag = 0

            if flag == 1:
                self.create_enemy(x, y, structure)
                break

    def rand_move_enemy(self, structure):
        rand_num = random.randint(1, 4)
        if rand_num == 1:
            self.move_up()
            if self.kill() == 1:
                return 1
            else:
                return 0
        elif rand_num == 2:
            self.move_down()
            if self.kill() == 1:
                return 1
            else:
                return 0
        elif rand_num == 3 and self.flag == 1:
            self.move_left()
            if self.kill() == 1:
                return 1
            else:
                return 0
        elif rand_num == 4 and self.flag == 1:
            self.move_right()
            if self.kill() == 1:
                return 1
            else:
                return 0

    def display_with_enemy(self, structure):

        for i in range(0, 42):
            for j in range(0, 84):
                print(structure[i][j], end="")
            print()

    def kill(self):

        # if self.structure[self.x+move_x][self.y+move_y] == '^':
        #     self.flag = 0
        #     for j in range(0,2):
        #         for i in range(0,4):
        #             self.shape[j][i]=' '
        #             self.structure[self.x+j][self.y+i] = self.shape[j][i]
        #
        #     return 1

        if self.structure[self.x][self.y] == '^':
            self.flag = 0
            for j in range(0, 2):
                for i in range(0, 4):
                    self.shape[j][i] = ' '
                    self.structure[self.x + j][self.y + i] = self.shape[j][i]

            return 1

        else:
            return 0
