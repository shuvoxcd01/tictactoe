import copy
import random

from tic_tac_toe.ai_agents.minimax_agent.minimax import MiniMax
from tic_tac_toe.envs.tic_tac_toe_base_env import TicTacToeBaseEnv


class TicTacToeEnvEpsilonStochastic(TicTacToeBaseEnv):
    def __init__(self):
        super(TicTacToeEnvEpsilonStochastic, self).__init__()
        self.epsilon = 0.7
        self.ai_engine = MiniMax()

    def _step(self, action):
        assert action in range(self.num_moves)

        if self.state[action] != 0:
            observation = copy.deepcopy(self.state)
            reward = -1.0
            done = False
            info = {}

            return observation, reward, done, info

        self.state[action] = 1 if self.player_to_move else -1
        self.player_to_move = not self.player_to_move

        computer_move = None

        if not self.is_game_over():
            if random.random() <= self.epsilon:
                computer_move = self.ai_engine.search(self())
            else:
                computer_move = random.choice(self.get_legal_moves())

            self.make_move(computer_move)

            if not self.is_game_over():
                observation = copy.deepcopy(self.state)
                reward = 0.0
                done = False
                info = {'computer_move': computer_move}
                return observation, reward, done, info

        observation = copy.deepcopy(self.state)
        reward = self.get_result(self.human_player)
        done = True
        info = {'computer_move': computer_move}

        return observation, reward, done, info
