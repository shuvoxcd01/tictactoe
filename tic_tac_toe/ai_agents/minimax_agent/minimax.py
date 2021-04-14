class MiniMax:
    def __init__(self):
        self.memory = {}
        self.max_player = None

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

        self.memory[env.get_state_as_key()] = (best_action, best_value)

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
                self.memory[env.get_state_as_key()] = (action, value)

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
                self.memory[env.get_state_as_key()] = (action, value)

        return value
