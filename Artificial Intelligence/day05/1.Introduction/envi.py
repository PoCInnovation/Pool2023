"""
In this file we define the environment class to avoid filling the notebook with too much code
"""
import random
import numpy as np

GRAPHICS = {' ': [255,  255, 255],
            'O': [255,  0,   0],
            'P': [0,    0,   255],
            'X': [0,    255, 0]}

REWARDS = {'NEGATIVE': -100,
           'NEUTRAL': -1,
           'POSITIVE': 1000}


class Environment:
    """
    The environment which will receive actions and update state
    """

    def __init__(self, map_size, actions):
        self.map_size = map_size
        self.actions = actions

        # generating a random map
        self.map = [' '] * self.map_size
        for i in range(self.map_size):
            self.map[i] = [' '] * self.map_size
            obstacle = random.randint(0, self.map_size - 1)
            for j in range(self.map_size):
                if i * self.map_size + j == self.map_size ** 2 - 1:
                    self.map[i][j] = 'X'
                    continue
                if i != 0 and i != self.map_size - 1 and j == obstacle:
                    self.map[i][j] = 'O'
                    obstacle = True
        # spawning obstacles
        self.dangers = []
        for y in range(self.map_size):
            for x in range(self.map_size):
                if self.map[y][x] == 'O':
                    self.dangers.append(y*self.map_size+x)
        # initialising agent state
        self.state = 0

    def graphic(self):
        """
        This method will return an array of colors which can be used for animation in matplotlib
        """
        color_array = [[GRAPHICS[x] for x in y] for y in self.map]
        color_array[self.state // self.map_size][self.state %
                                                 self.map_size] = GRAPHICS['P']
        return np.array(color_array).repeat(10, axis=0).repeat(10, axis=1)

    def step(self, action):
        """
        This method will update the environment based on the chosen action by the agent
        """
        new_state = self.state
        reward = 0
        done = False

        # movement
        if action == self.actions['UP']:
            new_state -= self.map_size
        if action == self.actions['DOWN']:
            new_state += self.map_size
        if action == self.actions['LEFT'] and new_state % self.map_size != 0:
            new_state -= 1
        if action == self.actions['RIGHT'] and new_state % self.map_size != self.map_size - 1:
            new_state += 1
        if 0 <= new_state < self.map_size ** 2:
            self.state = new_state
        # granting rewards
        reward = REWARDS['NEUTRAL']
        if self.state in self.dangers:
            reward = REWARDS['NEGATIVE']
            done = True
        if self.state == self.map_size ** 2 - 1:
            reward = REWARDS['POSITIVE']
            done = True
        return self.state, reward, done

    def reset(self):
        """
        This method resets our environment to default values
        """
        self.state = 0
        return self.state
