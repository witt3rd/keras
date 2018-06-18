import gym
import gym.spaces

# catalog installed environments
from gym import envs

print("Environments: {}".format(envs.registry.all()))

# load an environment
env = gym.make('CartPole-v0')

# how are the spaces defined?
print("Action space: {}".format(env.action_space))
print("Observation space: {}".format(env.observation_space))

# do stuff
for i_episode in range(20):
    observation = env.reset()
    for t in range(100):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break

# clean exit
env.close()
