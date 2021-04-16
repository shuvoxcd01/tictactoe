# tictactoe
A tictactoe environment to use with OpenAI gym. It is powered by MiniMax search algorithm. 

## Installation (Local)
Clone/(download and unarchive) the repo. From the parent directory, type the following line in the terminal.

pip install -e tictactoe

## Usage
Use it like a regular gym environment.
env = gym.make('tic_tac_toe:tic_tac_toe-v0')

Note that, the render method of this environment works in 'ansi' mode and returns a string. Just print the string to get a visualization of the current state of the game. 
