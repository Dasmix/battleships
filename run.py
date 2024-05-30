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
        

def new_game():

    size = 8
    num_ships = 5
    print("." * 35)
    print("Welcome to Battleships Game!")
    print("." * 35)
    print("Board size: {size}. Number of ships: {ships} ")