import random

class Board:

    def __init__(self, size, ships_num):
        
        self.size = size
        self.board = [["[~]" for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.guesses = []
        self.ships = []

    def place_ships(self):
    
        ships = []
        while len(ships) < self.num_ships:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            if (x, y) not in ships:
                ships.append((x, y))
        return ships

    def display(self, reveal=False):
        display_board = [row[:] for row in self.board]
        if reveal:
            for (x, y) in self.ships:
                display_board[x][y] = "[O]"
        for row in display_board:
            print(" ".join(row))


def new_game():

    size = 8
    num_ships = 5
    print ("""                                     # #  ( )
                                  ___#_#___|__
                              _  |____________|  _
                       _=====| | |            | | |==== _
                 =====| |.---------------------------. | |====
   <--------------------'   .  .  .  .  .  .  .  .   '--------------/
     \             Welcome to Battleships Game!                     /
      \____________________________________________________________/
  wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
   wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww """
    print("Board size: {size}. Number of ships: {ships} ")
    print("Your board:")
    player_board.display(reveal=True)
    print("Computer board:")
    computer_board.display()
