from person import *
from bomberman import *
from brick import *
from board import *
from alarmexception import *
from getchunix import *
import sys
import os
from enemy import *
from bomb import *

getch = GetchUnix()


def alarmHandler(signum, frame):
    raise AlarmException


def input_to(timeout=1):
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.alarm(timeout)
    try:
        text = getch()
        signal.alarm(0)
        return text
    except AlarmException:
        print("\n Prompt timeout. Continuing...")
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''


structure = [[0 for x in range(84)] for y in range(42)]

new_str = Board(structure)
new_str.board_structure(structure)

new_brick = []
for i in range(0, 20):
    temp_brick = Brick(structure)
    temp_brick.place_brick(structure)
    new_brick.append(temp_brick)

new_ene = []
enemy_count = 5
for i in range(0, 5):
    temp_ene = Enemy(structure)
    temp_ene.place_enemy(structure)
    new_ene.append(temp_ene)

bombs = []

new_bman = Bomberman(structure)

control = 0
score = 0

while True and enemy_count != 0 and new_bman.lives != 0:

    new_bman.die_respawn()

    os.system('tput reset')

    new_str.display_board(structure)

    print("Lives: ", end="")
    print(new_bman.lives, end="  ")

    print("Enemies: ", end="")
    print(enemy_count, end="  ")

    print("Score: ", end="")
    print(score)

    control = input_to()

    if control == 'q' or control == 'Q':
        sys.exit()

    elif control == 'w' or control == 'W':
        if new_bman.up_respawn() == 0:
            new_bman.move_up()

    elif control == 'a' or control == 'A':
        if new_bman.left_respawn() == 0:
            new_bman.move_left()

    elif control == 's' or control == 'S':
        if new_bman.down_respawn() == 0:
            new_bman.move_down()

    elif control == 'd' or control == 'D':
        if new_bman.right_respawn() == 0:
            new_bman.move_right()

    elif control == 'b' or control == 'B':
        new_bomb = Bomb(structure, new_bman.x, new_bman.y)
        new_bomb.create_bomb(structure)
        bombs.append(new_bomb)

    for i in range(0, len(bombs)):
        if bombs[i].flag == 0 and int(time.time()) - int(bombs[i].time) <= 0:
            bombs[i].tick(structure, 0)
        elif bombs[i].flag == 0 and int(time.time()) - int(bombs[i].time) <= 1:
            bombs[i].tick(structure, 1)
        elif bombs[i].flag == 0 and int(time.time()) - int(bombs[i].time) <= 2:
            bombs[i].tick(structure, 2)
        elif bombs[i].flag == 0:
            score = score + bombs[i].explode(structure)
            bombs[i].flag = 1
        elif bombs[i].flag == 1 and int(time.time()) - int(bombs[i].time) <= 4:
            bombs[i].vanish(structure)

    for i in range(0, len(new_ene)):
        if new_ene[i].rand_move_enemy(structure) == 1:
            enemy_count = enemy_count - 1
            score = score + 100

        new_bman.die_respawn()


if new_bman.lives == 0:
    os.system('tput reset')
    print("Game Over")
    print("Your score is : ", end="")
    print(score)

elif enemy_count == 0:
    os.system('tput reset')
    print("You Won")
    print("Your score is : ", end="")
    print(score)
