import random


class Brick():

    def __init__(self, structure):
        self.structure = structure

    def create_bricks(self, brick_x, brick_y, structure):
        for i in range(0, 2):
            for j in range(0, 4):
                structure[brick_x + i][brick_y + j] = '/'

    def place_brick(self, structure):
        brick_count = 0
        while True:
            y = random.randint(4, 76)
            x = random.randint(2, 38)
            flag = 1

            if x % 4 == 2 and (y % 8 == 0 or y % 8 == 4):
                flag = 1
            elif x % 4 == 0 and y % 8 == 4:
                flag = 1
            else:
                flag = 0

            if flag == 1:
                self.create_bricks(x, y, structure)
                break

    def display_with_bricks(self, structure):

        for i in range(0, 42):
            for j in range(0, 84):
                print(structure[i][j], end="")
            print()
