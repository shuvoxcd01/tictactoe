from gym.envs.registration import register

register(
    id='tic_tac_toe-v0',
    entry_point='tic_tac_toe.envs:TicTacToeEnv'
)
