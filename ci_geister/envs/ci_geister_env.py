import gym
from gym import error, spaces, utils
from gym.utils import seeding


class CIGetsterEnv(gym.Env):
    metadata = {"render.modes": ["human"]}

    def __init__(self):
        pass

    # actionを1ステップ実行し、結果を返す
    def step(self, action):
        pass

    # 状態を初期化し、初期盤面を返す
    def reset(self):
        pass

    # 環境を可視化する(暫くは不要)
    def render(self, mode="human", close=False):
        pass

    # 環境を終了する
    def close(self):
        pass

    # シード値を指定する
    def seed(self, seed=None):
        pass

