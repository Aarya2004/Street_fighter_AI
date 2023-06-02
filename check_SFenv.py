from stable_baselines3.common.env_checker import check_env
from SFenv import SFenv


env = SFenv()
check_env(env)