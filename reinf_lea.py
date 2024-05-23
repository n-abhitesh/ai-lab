import numpy as np

gamma = 0.9
theta = 1e-6
num_states = 10
num_actions = 2

V = np.zeros(num_states)

reward_matrix = np.random.rand(num_states, num_actions)
transition_matrix = np.zeros((num_states, num_actions), dtype=int)

for state in range(num_states):
    transition_matrix[state, 0] = (state + 1) % num_states
    transition_matrix[state, 1] = (state - 1) % num_states

def reward(state, action):
    return reward_matrix[state, action]

def next_state(state, action):
    return transition_matrix[state, action]

def value_iteration():
    while True:
        delta = 0
        for state in range(num_states):
            v = V[state] 
            max_value = float('-inf')
            for action in range(num_actions):
                next_s = next_state(state, action)
                r = reward(state, action)
                max_value = max(max_value, r + gamma * V[next_s])
            V[state] = max_value
            delta = max(delta, abs(v - V[state]))
        if delta < theta:
            break

def extract_policy():
    policy = np.zeros(num_states, dtype=int)
    for state in range(num_states):
        max_value = float('-inf')
        best_action = 0
        for action in range(num_actions):
            next_s = next_state(state, action)
            r = reward(state, action)
            value = r + gamma * V[next_s]
            if value > max_value:
                max_value = value
                best_action = action
        policy[state] = best_action
    return policy

value_iteration()
policy = extract_policy()

print("Optimal Value Function:")
print(V) 
print("Optimal Policy:")
print(policy)
