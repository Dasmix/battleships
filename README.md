![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)
# Battleships Game


![I am responsive](/battleshipr.png)
[View the live project here.](https://battleships-game1-8601e53e256f.herokuapp.com/)

# Battleships

Battleships is a Python terminal game, which runs in the Code Institute mock terminal on Heroku
Users can try to beat the computer by finding all of the computer's battleships before the computer finds theirs. Each
battleship occupies one square on the board.



## How to play

Battleships is based on the classic pen-and-paper game. You can read more about ił on [Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game)).
In this version, the player enters their name and two boards are randomly generated.
The player can see where their ships are, indicated by an [O] sign, but cannot see where the computer's ships are.
Guesses are marked on the board with an [X] . Hits are indicated by *.
The player and the computer then take it in turns to make guesses and try to Sink each other's battleships.
The winner is the player who sinks all of their opponenťs battleships first.

## Features

### Existing Features

- Random board generation
    - Ships are randomly placed on both the player and computer boards
    - The player cannot see where the computer's ships are

    ![boards](/battleshipboards.png)

    - Play against the computer
    - Accepts user input


    - Input validation and error-checking
        - You cannot enter coordinates outside the size of the gir
        - You cannot enter the same guess twice

        ![error-checking](/battleshiperrorchecking.png)


## Testing



I have manually tested this project by doing the following:
- Passed the code through PEP8 linter and confirmed are no problems
- Given invalid inputs: string when numbers are expected, out of bounds inputs, same input twice
- Tested in my local terminal and the CI Heroku terminal

## Bugs
- When a string is inadvertently inputted instead of numbers, the computer proceeds with its move regardless


## Deployment
This project was deployed using Code Institute's mock terminal for Heroku.
- Steps for deployment:
    - Fork or clone this repository
    - Create a new Heroku app
    - Set the buildbacks to Python and NodeJS in that order
    - Link the Heroku app to the repository
    - Click on Deploy
## Credits
- Code Institute for the deployment terminal
- Wikipedia for the details of the Battleships game
- Code Institute for README template
