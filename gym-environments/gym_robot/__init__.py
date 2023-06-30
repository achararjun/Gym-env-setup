from gym.envs.registration import register

register(id='Robot-v0',
         entry_point='gym_robot.envs:RobotEnv',
         )