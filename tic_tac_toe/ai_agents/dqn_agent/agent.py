import tensorflow as tf
import numpy as np

from tic_tac_toe.ai_agents.dqn_agent.saved_model import path_to_saved_model


class DQNAgent:
    def __init__(self):
        self.q_network = tf.keras.models.load_model(path_to_saved_model)

    def get_best_move(self, observation, player_to_move, legal_moves_mask):
        observation = np.append(observation, float(player_to_move))
        observation = tf.expand_dims(tf.identity(observation), 0)

        actions = self.q_network(observation)[0]

        min_q_value = tf.reduce_min(actions)
        max_q_value = tf.reduce_max(actions)
        actions = (actions - min_q_value) / (max_q_value - min_q_value)

        valid_actions = tf.multiply(actions, legal_moves_mask)
        best_action = tf.math.argmax(valid_actions, axis=0).numpy()

        return best_action
