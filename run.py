import random


class Board:

    def __init__(self, size, num_ships):
        self.size = size
        self.board = [["[~]" for _ in range(size)] for _ in range(size)]
        self.num_ships = num_ships
        self.guesses = set()
        self.ships = self.place_ships()

    def place_ships(self):
        """
        Randomly place ships on the board.
        """
        ships = []
        while len(ships) < self.num_ships:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            if (x, y) not in ships:
                ships.append((x, y))
        return ships

    def display(self, reveal=False):
        """
        Display the board.
        """
        display_board = [row[:] for row in self.board]
        if reveal:
            for (x, y) in self.ships:
                display_board[x][y] = "[O]"
        for row in display_board:
            print(" ".join(row))

    def take_shot(self, x, y):
        """
        Process a shot at the specified coordinates.
        """
        if (x, y) in self.ships:
            self.board[x][y] = "[X]"
            self.ships.remove((x, y))
            return "Hit!"
        else:
            self.board[x][y] = "[*]"
            return "Miss!"

    def player_turn(self, computer_board):
        """
        Handle the player's turn to take a shot at the computer's board.
        """
        try:
            print("Your turn:")
            while True:
                shot_x = int(input(f"Enter the row (0-{self.size - 1}) to take a shot: "))
                shot_y = int(input(f"Enter the column (0-{self.size - 1}) to take a shot: "))
                if (shot_x, shot_y) in self.guesses:
                    print("You've already shot that position. Please choose another.")
                elif 0 <= shot_x < self.size and 0 <= shot_y < self.size:
                    self.guesses.add((shot_x, shot_y))
                    result = computer_board.take_shot(shot_x, shot_y)
                    print(f"You {result}")
                    print("Computer's board:")
                    computer_board.display()
                    break
                else:
                    print(f"Invalid coordinates. Please enter values between 0 and {self.size-1}.")
        except ValueError:
            print("Invalid input. Please enter integer values.")

    def computer_turn(self, player_board):
        """
        Handle the computer's turn to take a shot at the player's board.
        """
        print("Computer's turn:")
        while True:
            comp_shot_x = random.randint(0, self.size - 1)
            comp_shot_y = random.randint(0, self.size - 1)
            if (comp_shot_x, comp_shot_y) not in player_board.guesses:
                player_board.guesses.add((comp_shot_x, comp_shot_y))
                break
        result = player_board.take_shot(comp_shot_x, comp_shot_y)
        print(f"Computer shot at ({comp_shot_x}, {comp_shot_y}) and {result}")
        print("Your board:")
        player_board.display(reveal=True)


def new_game():
    """
    Start a new game with default board size and number of ships.
    """
    size = 3
    num_ships = 5
    player_board = Board(size, num_ships)
    computer_board = Board(size, num_ships)
    """
    Print a welcome message and display initial game setup information.
    """
    print(
        """
                                     # #  ( )
                                  ___#_#___|__
                              _  |____________|  _
                       _=====| | |            | | |==== _
                 =====| |.---------------------------. | |====
   <--------------------'   .  .  .  .  .  .  .  .   '--------------/
     \             Welcome to Battleships Game!                     /
      \____________________________________________________________ /
  wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
   wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
        """
    )
    print(f"Board size: {size}. Number of ships: {num_ships} ")
    print("Your board:")
    player_board.display(reveal=True)
    print("Computer board:")
    computer_board.display()
    """
    Execute the game loop where player and computer take turns until one side
    loses all ships. Print appropriate messages based on the outcome.
    """
    while player_board.ships and computer_board.ships:
        player_board.player_turn(computer_board)
        if not computer_board.ships:
            break
        computer_board.computer_turn(player_board)
    if not computer_board.ships:
        print("Congratulations! You've sunk all the computer's ships.")
    else:
        print("Game over. The computer sunk all your ships.")


new_game()
