import copy

from tic_tac_toe.ai_agents.minimax_agent.minimax import MiniMax
from tic_tac_toe.envs.tic_tac_toe_base_env import TicTacToeBaseEnv


class TicTacToeEnvMiniMax(TicTacToeBaseEnv):
    def __init__(self):
        super(TicTacToeEnvMiniMax, self).__init__()
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
