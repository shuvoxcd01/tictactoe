import json
import os

from tic_tac_toe.ai_agents.minimax_agent import memory_file_path
from tic_tac_toe.envs.tic_tac_toe_base_env import TicTacToeBaseEnv


class MiniMax:
    def __init__(self):
        self.memory = self.get_or_create_memory()
        self.max_player = None

    def get_or_create_memory(self):
        if not os.path.exists(memory_file_path):
            self.create_memory()

        with open(memory_file_path, "r") as memory_file:
            memory = json.load(fp=memory_file)

        return memory

    def create_memory(self):
        env = TicTacToeBaseEnv()
        self.memory = {}

        assert env.get_state_as_key() == ('0000000001')
        self.search(env=env())

        env.player_to_move = False
        assert env.get_state_as_key() == ('0000000000')
        self.search(env=env())

        with open(memory_file_path, "w") as memory_file:
            json.dump(obj=self.memory, fp=memory_file)

    def search(self, env):
        if env.get_state_as_key() in self.memory:
            return self.memory[env.get_state_as_key()][0]

        self.max_player = env.player_to_move

        actions = env.get_legal_moves()

        assert actions != []

        min_values = []

        for action in actions:
            min_values.append(self.get_min_value(env().make_move(action)))

        best_value = max(min_values)
        best_action = actions[min_values.index(best_value)]

        self.memory[env.get_state_as_key()] = (int(best_action), float(best_value))

        return best_action

    def get_max_value(self, env):
        assert env.player_to_move == self.max_player

        if env.get_state_as_key() in self.memory:
            return self.memory[env.get_state_as_key()][1]

        if env.is_game_over():
            return env.get_result(self.max_player)

        value = float('-inf')

        for action in env.get_legal_moves():
            new_value = self.get_min_value(env().make_move(action))

            if new_value > value:
                value = new_value
                self.memory[env.get_state_as_key()] = (int(action), float(value))

        return value

    def get_min_value(self, env):
        assert env.player_to_move != self.max_player

        if env.get_state_as_key() in self.memory:
            return self.memory[env.get_state_as_key()][1]

        if env.is_game_over():
            return env.get_result(player=self.max_player)

        value = float('inf')

        for action in env.get_legal_moves():
            new_value = self.get_max_value(env().make_move(action))

            if new_value < value:
                value = new_value
                self.memory[env.get_state_as_key()] = (int(action), float(value))

        return value
