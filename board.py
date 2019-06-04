from termcolor import colored as clr


class Board():

    def __init__(self, structure):
        self.structure = structure

    def board_structure(self, structure):
        for i in range(0, 2):
            for j in range(0, 84):
                structure[i][j] = '#'

        for i in range(40, 42):
            for j in range(0, 84):
                structure[i][j] = '#'

        for i in range(2, 40):
            if i % 4 == 2 or i % 4 == 3:
                for j in range(0, 4):
                    structure[i][j] = '#'

                for j in range(4, 80):
                    structure[i][j] = ' '

                for j in range(80, 84):
                    structure[i][j] = '#'

            elif i % 4 == 0 or i % 4 == 1:
                for j in range(0, 4):
                    structure[i][j] = '#'
                for j in range(80, 84):
                    structure[i][j] = '#'
                for j in range(4, 80):
                    if j % 8 in range(0, 4):
                        structure[i][j] = '#'
                    else:
                        structure[i][j] = ' '

    def display_board(self, structure):

        for i in range(0, 42):
            for j in range(0, 84):
                if structure[i][j] == '#':
                    print(clr(structure[i][j], "cyan"), end="")
                elif structure[i][j] == 'B':
                    print(clr(structure[i][j], "green"), end="")
                elif structure[i][j] == 'E':
                    print(clr(structure[i][j], "red"), end="")
                elif structure[i][j] == '^':
                    print(clr(structure[i][j], "yellow"), end="")
                elif structure[i][j] == '/':
                    print(clr(structure[i][j], "magenta"), end="")
                else:
                    print(structure[i][j], end="")
            print()
