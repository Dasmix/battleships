![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Battleships

Battleships is a Python terminal game, which runs in the Code Institute mock terminal on Heroku
Users can try to beat the computer by finding all of the computer's battleships before the computer finds theirs. Each
battleship occupies one square on the board.



## How to play

Battleships is based on the classic pen-and-paper game. You can read more about ił on Wikipedia.
In this version, the player enters their name and two boards are randomly generated.
The player can see where their ships are, indicated by an @ sign, but cannot see where the computer's ships are.
Guesses are marked on the board with an x . Hits are indicated by
The player and the computer then take ił in turns to make guesses and try to Sink each other's battleships.
The winner is the player who sinks all of their opponenťs battleships first.

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!
