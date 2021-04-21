from gym.envs.registration import register

register(
  id='ci-geister-v0'
  entry_point='ci_gester.envs.CIGetsterEnv',
)