import mujoco as mj
import gym
from gym import spaces
import pygame
import os
import numpy as np
class RobotEnv(gym.Env):
    def __init__(self):
        metadata = {
        "render_modes": [
            "human",
            "rgb_array",
            "depth_array",
        ],
        "render_fps": 20,
    }
        dirname = os.path.dirname(__file__)
        mujoco_path = 'robot.xml'
        abspath = os.path.join(dirname + "/" + mujoco_path)
        mujoco_path = abspath
        self.model = mj.MjModel.from_xml_path(mujoco_path)
        self.observation_space = spaces.Discrete(5)
        self.action_space = spaces.Discrete(4)

    def _get_obs(self):
       return 0

    def _get_info(self):
       return {}
   
    def reset(self, seed=None, options=None):
       super().reset(seed=seed)
       observation = self._get_obs()
       info = self._get_info()
       if self.render_mode == "human":
            self._render_frame()
       return observation, info

    def step(self,action):
       observation = self._get_obs()
       info = self._get_info()
       reward=1
       terminated=0
       return observation, reward, terminated, False, info

    def render(self,):
       if self.render_mode == "rgb_array":
            return self._render_frame()
         
    def _render_frame(self):
        if self.render_mode == "human":
            self._get_viewer(self.render_mode).render()
            
          

    def close(self):
       if self.window is not None:
            pygame.display.quit()
            pygame.quit()
            
    def _reset_simulation(self):
        self.sim.reset()


