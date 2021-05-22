from tic_tac_toe.ai_agents.minimax_agent import memory_file_path
from tic_tac_toe.ai_agents.minimax_agent.minimax import MiniMax
from tic_tac_toe.envs import TicTacToeEnvMiniMax
import json


def create_memory():
    env = TicTacToeEnvMiniMax()
    minimax = MiniMax()

    assert env.get_state_as_key() == ('0000000001')
    minimax.search(env=env())

    env.player_to_move = False
    assert env.get_state_as_key() == ('0000000000')
    minimax.search(env=env())

    with open(memory_file_path, "w") as memory_file:
        json.dump(obj=minimax.memory, fp=memory_file)


if __name__ == "__main__":
    create_memory()
