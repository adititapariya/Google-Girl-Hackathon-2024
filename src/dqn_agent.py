# src/dqn_agent.py

#This file contains the implementation of the DQN agent, which is responsible for learning and decision-making within the NOC environment.

#DQNAgent Class:
#Initialization: Initializes the DQN agent with parameters such as state size and action size.
#Build Model: Defines and compiles the Q-network using TensorFlow/Keras, which approximates the Q-value function.
#Act Method: Implements the epsilon-greedy policy for action selection based on the current state and Q-values.
    
import numpy as np
import tensorflow as tf

class DQNAgent:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size
        self.model = self.build_model()

    def build_model(self):
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(64, activation='relu', input_shape=(self.state_size,)),
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dense(self.action_size, activation='linear')
        ])
        model.compile(optimizer='adam', loss='mse')
        return model

    def act(self, state, epsilon=0):
        if np.random.rand() <= epsilon:
            return np.random.choice(self.action_size)
        q_values = self.model.predict(state)
        return np.argmax(q_values[0])
