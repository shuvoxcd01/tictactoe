from gym.envs.registration import register

register(
    id='tic_tac_toe-minimax-v0',
    entry_point='tic_tac_toe.envs:TicTacToeEnvMiniMax'
)

register(
    id='tic_tac_toe-epsilon_stochastic-v0',
    entry_point='tic_tac_toe.envs:TicTacToeEnvEpsilonStochastic'
)

register(
    id='tic_tac_toe-stochastic-v0',
    entry_point='tic_tac_toe.envs:TicTacToeEnvStochastic'
)
