# tictactoe

A tictactoe environment to use with OpenAI gym.

## Dependencies

Python version used = 3.8   
See _requirements.txt_ for dependencies.

## Installation (Local)

Clone/(download and unarchive) the repo. From the parent directory, type the following line in the terminal.

`pip install -e tictactoe`

## Usage

Use it like a regular gym environment.
`env = gym.make('tic_tac_toe:tic_tac_toe-v0')`

There are 4 environments in this package.

1. Stochastic environment (default).
2. Semi-stochastic environment.
3. Minimax environment.
4. DQN environment.

**Stochastic environment:**     
Instantiation:  
`env = gym.make('tic_tac_toe:tic_tac_toe-v0')`  
or  
`env = gym.make('tic_tac_toe:tic_tac_toe-stochastic-v0')`

_The environment selects action randomly._

**Semi-stochastic environment:**    
Installation:   
`env = gym.make('tic_tac_toe:tic_tac_toe-epsilon_stochastic-v0')`

_The environment selects action according to an ai engine (Minimax) with probability epsilon (0.7) and selects a random
action with probability 1 - epsilon._

**Minimax environment:**    
Installation:   
`env = gym.make('tic_tac_toe:tic_tac_toe-minimax-v0')`

_The environment selects action according to the Minimax algorithm._

**DQN environment:**    
Installation:   
`env = gym.make('tic_tac_toe:tic_tac_toe-dqn-v0')`

_The environment selects action according to a pre-trained DQN agent._

Example:    
`env = gym.make('tic_tac_toe:tic_tac_toe-epsilon_stochastic-v0') `
`env.set_player_to_move_first("me")`  
`env.reset()`
`done = False`

`print(env.render())`

`while not done: `  
`....human_move = int(input("Choose a move from " + str(env.get_legal_moves())))`     
`....obs, reward, done, info = env.step(human_move) `   
`....print(env.render())`

## Reward policy:

+1 for win, -1 for loss, 0 for draw and all other states except when the selected action has already been selected
previously. Then the reward is -1.

## Rendering:

Note that, the render method of this environment works in 'ansi' mode and returns a string. Just print the string to get
a visualization of the current state of the game. 
