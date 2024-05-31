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

    def take_shot(self, x, y):
        if (x, y) in self.ships:
            self.board[x][y] = "[X]"
            self.ships.remove((x, y))
            return "Hit!"
        else:
            self.board[x][y] = "[*]"
            return "Miss!"

    def player_turn(computer_board, size):
    try:
        print("Your turn:")
        shot_x = int(input("Enter the row (0-7) to take a shot: "))
        shot_y = int(input("Enter the column (0-7) to take a shot: "))
        if 0 <= shot_x < size and 0 <= shot_y < size:
            result = computer_board.take_shot(shot_x, shot_y)
            print(f"You {result}")
            print("Computer's board:")
            computer_board.display()
        else:
            print("Invalid coordinates. Please enter values between 0 and 7.")
            player_turn(computer_board, size)  
    except ValueError:
        print("Invalid input. Please enter integer values.")
        player_turn(computer_board, size)  

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
