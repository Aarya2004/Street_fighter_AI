import gym
from gym import spaces
from pyboy import PyBoy, WindowEvent
from collections import deque
import numpy as np

MAX_PREV_ACTIONS = 30
    
class SFenv(gym.Env):
    """Custom Environment that follows gym interface"""

    total_reward = 0

    def __init__(self):
        super(SFenv, self).__init__()
        self.action_space = spaces.MultiDiscrete(np.array([ 4, 2, 2 ]))
        self.observation_space = spaces.Box(low=-1, high=255,
                                            shape=(6+MAX_PREV_ACTIONS,), dtype=np.int64)

    def step(self, action):
        for button_action in action:
            self.prev_actions.append(button_action)
        self.game.send_input(WindowEvent.PRESS_SPEED_UP)
        self.game.tick()
        self.game.send_input(WindowEvent.RELEASE_SPEED_UP)

        button_pressed = action[0]
        if button_pressed == 0:
            self.game.send_input(WindowEvent.PRESS_ARROW_DOWN)
        elif button_pressed == 1:
            self.game.send_input(WindowEvent.PRESS_ARROW_LEFT)
        elif button_pressed == 2:
            self.game.send_input(WindowEvent.PRESS_ARROW_UP)
        elif button_pressed == 3:
            self.game.send_input(WindowEvent.PRESS_ARROW_RIGHT)

        button_pressed = action[1]
        if button_pressed == 0:
            self.game.send_input(WindowEvent.RELEASE_BUTTON_A)
        else:
            self.game.send_input(WindowEvent.PRESS_BUTTON_A)
            
        button_pressed = action[2]
        if button_pressed == 0:
            self.game.send_input(WindowEvent.RELEASE_BUTTON_B)
        else:
            self.game.send_input(WindowEvent.PRESS_BUTTON_B)

        player_x_position = self.game.get_memory_value(0xC421)
        timer = self.game.get_memory_value(0xCBB3)
        player_health = self.game.get_memory_value(0xC3E2)
        opponent_health = self.game.get_memory_value(0xC3E4)
        opponent_x_position = self.game.get_memory_value(0xC621)
        distance_between_players = abs(player_x_position - opponent_x_position)
        initial_reward = 0

        if timer == 80:
            self.done = True
            self.game.stop()
            if opponent_health != 0:
                initial_reward = -9000
        if player_health == 0:
            self.done = True
            initial_reward = -10000
            self.game.stop()
        if opponent_health == 0:
            self.done = True
            initial_reward = 10000
            self.game.stop()


        self.total_reward = initial_reward + (player_health * 10) + (opponent_health * -10)
        
        info = {}

        self.player_health = player_health
        self.opponent_health = opponent_health

        observation = [timer, player_health, opponent_health, player_x_position, opponent_x_position, distance_between_players] + list(self.prev_actions)
        observation = np.array(observation)  

        return observation, self.total_reward, self.done, info
    
    def reset(self):
        self.game = PyBoy('________________') #Enter path to ROM File of Street Fighter Alpha: Warriors' Dream
        self.state_file = open("________________", "rb") #Enter path to ROM File of Street Fighter Alpha: Warriors' Dream
        self.game.load_state(self.state_file)
        player_x_position = self.game.get_memory_value(0xC421)
        timer = self.game.get_memory_value(0xCBB3)
        player_health = self.game.get_memory_value(0xC3E2)
        opponent_health = self.game.get_memory_value(0xC3E4)
        opponent_x_position = self.game.get_memory_value(0xC621)
        self.prev_button_pressed = 1
        self.button_pressed = 1


        self.total_reward = 0
        self.done = False
        distance_between_players = abs(player_x_position - opponent_x_position)

        self.prev_actions = deque(maxlen=MAX_PREV_ACTIONS)
        for i in range(MAX_PREV_ACTIONS):
            self.prev_actions.append(-1)

        observation = [timer, player_health, opponent_health, player_x_position, opponent_x_position, distance_between_players] + list(self.prev_actions)
        observation = np.array(observation)

        return observation