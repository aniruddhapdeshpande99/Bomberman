GAME : Bomberman
AUTHOR : Aniruddha Deshpande (20161058)
DESCRIPTION : Game of single player Bomberman

-----------------------------------------------------

REQUIREMENTS:

1. python3 compiler
2. python-termcolor module

-----------------------------------------------------

ENTITIES:

1. Wall : ####
          ####

2. Bricks : ////
            ////

3. Bomberman : BBBB
               BBBB

4. Enemy : EEEE
           EEEE

5. Bomb : [NN]
          [NN] where N is countdown number.

6. Explosion : ^^^^
               ^^^^

-----------------------------------------------------

INSTRUCTIONS :

1. To Run the game enter the following line :

   python3 main.py

2. Controls:

   W : Move Up
   A : Move Left
   S : Move Down
   D : Move Right
   B : Plant Bomb

3. You have 3 lives and unlimited Bombs.

4. You lose a life if you get caught in an explosion or if a randomly moving enemy kills you.

5. Game is over when you lose all the 3 lives.

6. You win if you kill all the 5 Enemies using your bombs.

7. Exploding a brick will fetch you 20 points.

8. Killing an enemy will fetch you 100 points.

-----------------------------------------------------

FEATURES IMPLEMENTED :

1. Polymorphism : Different kill functions used for Enemy and Bomberman. Bomberman also has the added   functionality of respawning if lives are available.

2. Encapsulation : Uses of classes implements the concept of encapsulation where in all the methods are encapsulated.

3. Inheritance : Person class is used as the parent class for Enemy and Bomberman which inherit the movement functionality.

4. Modularity : The whole game is divided into different modules (ie. classes) to implement modularity.

-----------------------------------------------------

BONUS FEATURES IMPLEMENTED :

1. Different color code for different entities within the game.

2. Bomb countdown to explosion displayed. 
