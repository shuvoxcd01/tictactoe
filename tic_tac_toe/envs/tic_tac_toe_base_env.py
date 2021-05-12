import copy
from abc import abstractmethod

import gym
import numpy as np
from gym import spaces


class TicTacToeBaseEnv(gym.Env):
    metadata = {'render.modes': ['ansi']}

    def __init__(self):
        super(TicTacToeBaseEnv, self).__init__()
        self.action_space = spaces.Discrete(9)
        self.observation_space = spaces.Box(low=-1, high=1, shape=(9,), dtype=np.int32)
        self.num_moves = 9

        self.human_player = True
        self.ai_player = False

        self.state = np.zeros(shape=(9,))
        self.player_to_move = self.human_player

        self.max_step_per_episode = 20
        self.num_step = 0

    def __call__(self):
        return copy.deepcopy(self)

    @abstractmethod
    def _step(self, action):
        raise NotImplementedError()

    def step(self, action):
        observation, reward, done, info = self._step(action)
        self.num_step += 1

        if self.num_step > self.max_step_per_episode:
            done = True

        return observation, reward, done, info

    def reset(self):
        self.num_step = 0
        self.state = np.zeros(shape=(9,))
        self.player_to_move = self.human_player

        observation = copy.deepcopy(self.state)

        return observation

    def render(self, mode='ansi'):
        if mode != 'ansi':
            super(TicTacToeBaseEnv, self).render()

        board = ""
        for i in range(self.num_moves):
            board += ".X0"[int(self.state[i])]
            if i % 3 == 2:
                board += "\n"

        return board

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
                    return 10.0
                else:
                    return -10.0
        return 0.0
