import numpy as np

gamma = 0.9
num_states = 10
num_actions = 2

Q = np.zeros((num_states, num_actions))

def reward(state, action):
    return np.random.rand()

def next_state(state, action):
    return (state + action) % num_states

def bellman_update(state, action, reward, next_state):
    best_next_action = np.argmax(Q[next_state, :])
    Q[state, action] = reward + gamma * Q[next_state, best_next_action]

for episode in range(1000):
    state = np.random.randint(num_states)
    while True:
        action = np.random.randint(num_actions)
        next_s = next_state(state, action)
        r = reward(state, action)
        bellman_update(state, action, r, next_s)
        state = next_s
        if state == 0:
            break

print("Q-Table after applying Bellman updates:")
print(Q)
