import copy

import gym
import numpy as np
from gym import spaces

from tic_tac_toe.ai_agents.minimax_agent.minimax import MiniMax


class TicTacToeEnv(gym.Env):
    metadata = {'render.modes': ['ansi']}

    def __init__(self):
        super(TicTacToeEnv, self).__init__()
        self.action_space = spaces.Discrete(9)
        self.observation_space = spaces.Box(low=-1, high=1, shape=(9,), dtype=np.int32)
        self.num_moves = 9

        self.human_player = True
        self.ai_player = False

        self.state = np.zeros(shape=(9,))
        self.player_to_move = self.human_player

        self.ai_engine = MiniMax()

    def __call__(self):
        return copy.deepcopy(self)

    def step(self, action):
        assert action in range(self.num_moves)

        if self.state[action] != 0:
            observation = copy.deepcopy(self.state)
            reward = -1.0
            done = False
            info = {}

            return observation, reward, done, info

        self.state[action] = 1 if self.player_to_move else -1
        self.player_to_move = not self.player_to_move

        ai_move = None

        if not self.is_game_over():
            ai_move = self.ai_engine.search(self())
            self.make_move(ai_move)
            if not self.is_game_over():
                observation = copy.deepcopy(self.state)
                reward = 0.0
                done = False
                info = {'computer_move': ai_move}
                return observation, reward, done, info

        observation = copy.deepcopy(self.state)
        reward = self.get_result(self.human_player)
        done = True
        info = {'computer_move': ai_move}

        return observation, reward, done, info

    def reset(self):
        self.state = np.zeros(shape=(9,))
        self.player_to_move = self.human_player

    def render(self, mode='ansi'):
        super(TicTacToeEnv, self).render()

    def is_game_over(self):
        for (x, y, z) in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]:
            if self.state[x] == self.state[y] == self.state[z] != 0:
                return True

        return np.all(self.state)

    def get_legal_moves_mask(self):
        moves = np.zeros(shape=self.num_moves)

        if self.is_game_over():
            return moves

        for i in range(self.num_moves):
            if self.state[i] == 0:
                moves[i] = 1

        return moves

    def get_legal_moves(self):
        return np.nonzero(self.get_legal_moves_mask())[0]

    def get_state_as_key(self):
        str_repr = ""
        for i in range(self.num_moves):
            str_repr += ["0", "1", "-1"][int(self.state[i])]

        key = (str_repr, self.player_to_move)
        return key

    def make_move(self, move):
        assert move in range(self.num_moves)

        assert self.state[move] == 0

        self.state[move] = 1 if self.player_to_move else -1
        self.player_to_move = not self.player_to_move

        return self

    def get_result(self, player):
        assert self.is_game_over()

        player = 1 if player else -1

        for (x, y, z) in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]:
            if self.state[x] == self.state[y] == self.state[z] != 0:
                if self.state[x] == player:
                    return 1.0
                else:
                    return -1.0
        return 0.0
