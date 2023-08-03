import sys
import pathlib

sys.path.append(str(pathlib.Path(__file__).parent))
sys.path.append(str(pathlib.Path(__file__).parent.parent))

import common


from common.dmc2gym import make_dmc_env
from PIL import Image
import time

if __name__ == '__main__':
    env = make_dmc_env()

    env.reset()
    while True:
        time.sleep(1)
        action = env.action_space.sample()
        obs, reward, done, info = env.step(action)
