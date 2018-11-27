import gym
import numpy as np

env = gym.make('CartPole-v0')
env.reset()

def get_action(s, w):
	return 1 if s.dot(w) > 0 else 0

def play_one_episode(env, params):
	observation = env.reset()
	done = False
	t = 0

	while not done and t<10000:
		#env.render()
		t += 1
		action = get_action(observation, params)
		observation, _, done, _ = env.step(action)
		if done:
			break  
	return t

def play_multiple_episodes(env, T, params):
	episode_lengths = np.empty(T)

	for i in range(T):
		episode_lengths[i] = play_one_episode(env, params)

	average_length = episode_lengths.mean()
	print("Average Length: {}".format(average_length))
	return average_length

def play_one_episode2(env, params):
	observation = env.reset()
	done = False
	t = 0

	while not done and t<10000:
		env.render()
		t += 1
		action = get_action(observation, params)
		observation, _, done, _ = env.step(action)
		if done:
			break  import gym
import numpy as np

env = gym.make('CartPole-v0')
env.reset()

def get_action(s, w):
	return 1 if s.dot(w) > 0 else 0

def play_one_episode(env, params):
	observation = env.reset()
	done = False
	t = 0

	while not done and t<10000:
		#env.render()
		t += 1
		action = get_action(observation, params)
		observation, _, done, _ = env.step(action)
		if done:
			break  
	return t

def play_multiple_episodes(env, T, params):
	episode_lengths = np.empty(T)

	for i in range(T):
		episode_lengths[i] = play_one_episode(env, params)

	average_length = episode_lengths.mean()
	print("Average Length: {}".format(average_length))
	return average_length

def play_one_episode2(env, params):
	observation = env.reset()
	done = False
	t = 0

	while not done and t<10000:
		env.render()
		t += 1
		action = get_action(observation, params)
		observation, _, done, _ = env.step(action)
		if done:
			break  
	return t

def play_multiple_episodes2(env, T, params):
	episode_lengths = np.empty(T)

	for i in range(T):
		episode_lengths[i] = play_one_episode2(env, params)

	average_length = episode_lengths.mean()
	print("Average Length: {}".format(average_length))
	return average_length

def random_search(env):
    episode_lengths = []
    best = 0
    params = None
    for t in range(100):
        new_params = np.random.random(4)*2 - 1
        avg_length = play_multiple_episodes(env, 100, new_params)
        episode_lengths.append(avg_length)
        if avg_length > best:
        	params = new_params
        	best = avg_length
    return episode_lengths, params



env = gym.make('CartPole-v0')
episode_lengths, params = random_search(env)

print("Final Run with Optimal Weights:")
play_multiple_episodes2(env, 100, params)
	return t

def play_multiple_episodes2(env, T, params):
	episode_lengths = np.empty(T)

	for i in range(T):
		episode_lengths[i] = play_one_episode2(env, params)

	average_length = episode_lengths.mean()
	print("Average Length: {}".format(average_length))
	return average_length

def random_search(env):
    episode_lengths = []
    best = 0
    params = None
    for t in range(100):
        new_params = np.random.random(4)*2 - 1
        avg_length = play_multiple_episodes(env, 100, new_params)
        episode_lengths.append(avg_length)
        if avg_length > best:
        	params = new_params
        	best = avg_length
    return episode_lengths, params



env = gym.make('CartPole-v0')
episode_lengths, params = random_search(env)

print("Final Run with Optimal Weights:")
play_multiple_episodes2(env, 100, params)
