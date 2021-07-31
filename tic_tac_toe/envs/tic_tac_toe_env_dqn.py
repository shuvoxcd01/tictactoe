import copy

from tic_tac_toe.ai_agents.dqn_agent.agent import DQNAgent
from tic_tac_toe.envs.tic_tac_toe_base_env import TicTacToeBaseEnv


class TicTacToeEnvDQN(TicTacToeBaseEnv):
    def __init__(self):
        super(TicTacToeEnvDQN, self).__init__()
        self.ai_agent = DQNAgent()

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
            observation = copy.deepcopy(self.state)
            player_to_move = not copy.deepcopy(self.player_to_move)
            legal_moves_mask = copy.deepcopy(self.get_legal_moves_mask())
            ai_move = self.ai_agent.get_best_move(observation, player_to_move, legal_moves_mask)
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
